package edu.iu.simplepagerank;

import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;

import edu.iu.harp.keyval.Long2DoubleKVPartition;
import edu.iu.harp.keyval.Long2DoubleKVTable;
import edu.iu.harp.partition.Partition;
import it.unimi.dsi.fastutil.longs.Long2DoubleOpenHashMap;
import it.unimi.dsi.fastutil.longs.LongIterator;
import it.unimi.dsi.fastutil.longs.LongSet;
import it.unimi.dsi.fastutil.objects.ObjectCollection;
 
public class Utils {

	 //for testing
    static void printLong2DoubleKVTable(Long2DoubleKVTable prTable) {
    	
     
    	
    	for(Partition<Long2DoubleKVPartition> aPartition: prTable.getPartitions()){
    		Long2DoubleKVPartition par = aPartition.get();
    		Long2DoubleOpenHashMap hm = par.getKVMap();
    		LongSet ls = hm.keySet();
    		LongIterator ltr = ls.iterator();
    		while(ltr.hasNext()){
    			long key = ltr.next();
    			double pr = hm.get(key);
    			System.out.println(key+": "+pr);
    		}
			
		}
    }
    
    
    static void printGraph(Map<Long, ArrayList<Long>> graph){
    	for (Entry<Long, ArrayList<Long>> entry : graph.entrySet()) {
		    Long sourceUrl = entry.getKey();
		    ArrayList<Long> targetUrls = entry.getValue();
		    
		    System.out.print(sourceUrl+":  ");
		    if(targetUrls != null){
		    	for(int i=0; i<targetUrls.size(); i++){
		    		System.out.print(targetUrls.get(i)+" ");
		    	}
		    }
		    System.out.println();
		}
    }
}

