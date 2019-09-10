package edu.iu.simplepagerank;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.CollectiveMapper;

import edu.iu.harp.keyval.Long2DoubleKVPartition;
import edu.iu.harp.keyval.Long2DoubleKVTable;
import edu.iu.harp.keyval.TypeDoubleCombiner;
import edu.iu.harp.partition.Partition;
import it.unimi.dsi.fastutil.longs.Long2DoubleOpenHashMap;
import it.unimi.dsi.fastutil.longs.LongIterator;
import it.unimi.dsi.fastutil.longs.LongSet;
 
public class PageRankMapper extends CollectiveMapper<String, String, LongWritable, Text> {
	
	int numUrls;
	int noIterations;
	
	public void setup(Context context) {
		Configuration conf = context.getConfiguration();
		numUrls = conf.getInt(PageRankConstants.NUM_URLS, 1);
		noIterations = conf.getInt(PageRankConstants.NUM_ITERATONS, 0);
	}
	/* Each mapCollective task handles one adjacency matrix in a split
	 * key: file offset. We do not really use the key
	 * value: <sourceUrl targetUrl-list>
	 */
	public void mapCollective( KeyValReader reader, Context context) throws IOException, InterruptedException {
		
		//STEP 0
		
		List<String> inputFiles = new ArrayList<String>();
	    while (reader.nextKeyValue()) {
	    	String key = reader.getCurrentKey();
	    	String value = reader.getCurrentValue();
	    	LOG.info("Key: " + key + ", Value: " + value);
	    	inputFiles.add(value);
	    }
		
		
		//STEP 1
		//each map-collective will load partial of graph data.
		Map<Long, ArrayList<Long>> partialGraph = new HashMap<Long, ArrayList<Long>>();
		loadPartialGraph(inputFiles, context.getConfiguration(), partialGraph);
		
		//STEP 2 initializing local pagerank table
		Long2DoubleKVTable initPRTable = new Long2DoubleKVTable(0,new TypeDoubleCombiner());
		initPRTable(partialGraph, initPRTable);
		allgather("harp-kmeans",  "allgather_initPRTable",initPRTable);
		System.out.println("Initial: ");
		Utils.printLong2DoubleKVTable(initPRTable);
		
		//STEP 3
		//Iterations
		// using localPRTable to store previous results;
		// using globalPRTable to store current results.
		Long2DoubleKVTable localPRTable = initPRTable;
		Long2DoubleKVTable globalPRTable=null;
		for(int i=0; i<noIterations; i++){
			
			globalPRTable = new Long2DoubleKVTable(1, new TypeDoubleCombiner() );
			
			// compute pagerank using previous results (localPRTable);
			// the new partial pagerank will be in the globalPRTable
			computePartialPR(partialGraph,  localPRTable,  globalPRTable );
			
			//test before allgather
			System.out.println("before Allgather");
			Utils.printLong2DoubleKVTable(globalPRTable);
			
			// all reduce pagerank tables
			allreduce("harp-kmeans",  "allgather_"+i,globalPRTable);
			
			//update pagerank
			updatePRTable(globalPRTable);
			
			//test printing intermidiate results.
			System.out.println("Iteration: "+i);
			Utils.printLong2DoubleKVTable(globalPRTable);
			
			//synchronize pagerank values
			localPRTable = globalPRTable;
		}

		// write to HDFS
		if(isMaster()){
			writePRToHDFS(globalPRTable, context);
		}
	}
	
	public void writePRToHDFS(Long2DoubleKVTable globalPRTable, Context context) throws IOException, InterruptedException{
		
		for(Partition<Long2DoubleKVPartition> aPartition: globalPRTable.getPartitions()){
    		Long2DoubleKVPartition par = aPartition.get();
    		Long2DoubleOpenHashMap hm = par.getKVMap();
    		LongSet ls = hm.keySet();
    		LongIterator ltr = ls.iterator();
    		while(ltr.hasNext()){
    			long key = ltr.next();
    			double pr = hm.get(key);
    			context.write(new LongWritable(key), new Text(pr+""));
    		}
		}
		
	}
	public void updatePRTable( Long2DoubleKVTable globalPRTable){
		
		for(Partition<Long2DoubleKVPartition> aPartition: globalPRTable.getPartitions()){
    		Long2DoubleKVPartition par = aPartition.get();
    		Long2DoubleOpenHashMap hm = par.getKVMap();
    		LongSet ls = hm.keySet();
    		LongIterator ltr = ls.iterator();
    		while(ltr.hasNext()){
    			long key = ltr.next();
    			double sumOfRankValues = hm.get(key);
    			double newPR =  0.85*sumOfRankValues+0.15*(1.0)/(double)numUrls;
    			//addKeyVal will add the value in the table. So firstly remove the keyvalue, then add new keyvalues
    			// currently key equals to partitionID.
    			globalPRTable.removePartition((int)key);
    			globalPRTable.addKeyVal(key, newPR);
    		}
		}
	}
	
	public void computePartialPR(Map<Long, ArrayList<Long>> partialGraph, Long2DoubleKVTable localPRTable, Long2DoubleKVTable globalPRTable){
		
		for (Entry<Long, ArrayList<Long>> entry : partialGraph.entrySet()) {
		    Long sourceUrl = entry.getKey();
		    ArrayList<Long> targetUrls = entry.getValue();
		    System.out.println("sourceURL: "+sourceUrl);
		    if(targetUrls == null ){
		    	// simply assume that the IDs of pages are: 0,1,2,...,(numUrls-1)
		    	System.out.println("targetUrls is null");
		    	double pr = localPRTable.getVal(sourceUrl) / numUrls;
		    	// TODO - Write Code
				// Add pr to the page rank of all other URLs in globalPRTable
				// Note. The addKeyVal(key, val) method in globalPRTable will
				// automatically sum values if the key exists. If the key does
				// NOT exist then a new entry will be made.
		    	 
		    	
		    }else{
		    	int numOfOutLinks = targetUrls.size();
		    	double pr = localPRTable.getVal(sourceUrl) / numOfOutLinks;
		    	// TODO - Write Code
				// Add pr to the page rank of all target URLs.
		    	 
		    	
		    }
		}
	}
	
	
	public void initPRTable(Map<Long, ArrayList<Long>> partialGraph, Long2DoubleKVTable localPRTable  ){
		for (Entry<Long, ArrayList<Long>> entry : partialGraph.entrySet()) {
		    Long sourceUrl = entry.getKey();
		    localPRTable.addKeyVal(sourceUrl, 1.0 / numUrls);
		}
	}

	public void loadPartialGraph( List<String> inputFiles, Configuration conf, Map<Long, ArrayList<Long>> partialGraph) throws IOException, InterruptedException{
		 
			for(String filename: inputFiles){
				FileSystem fs = FileSystem.get(conf);
				Path dPath = new Path(filename);
				FSDataInputStream in = fs.open(dPath);
				BufferedReader br = new BufferedReader( new InputStreamReader(in));
				String line="";
				String[] valArr=null;
				while((line = br.readLine()) != null){
					valArr = line.split("\\s+");
			
					if(valArr.length == 1){
						partialGraph.put(Long.parseLong(valArr[0]), null);
					}else{
						ArrayList<Long> targetUrls = new ArrayList<Long>();
						for(int i=1; i<valArr.length; i++){
							targetUrls.add(Long.parseLong(valArr[i]));
						}
						partialGraph.put(Long.parseLong(valArr[0]), targetUrls);
					}
				}
		}
	}
}
