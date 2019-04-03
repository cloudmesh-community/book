/*
 * The part 2 of project#1 for B534 class 2011
 * Hadoop PageRank   
 *  
 * @author Hui Li (lihui@indiana.edu)
 * 1/21/2010 
 */

package indiana.cgl.hadoop.pagerank;

import indiana.cgl.hadoop.pagerank.helper.CleanupResultsMap;
import indiana.cgl.hadoop.pagerank.helper.CleanupResultsReduce;
import indiana.cgl.hadoop.pagerank.helper.CreateGraphMap;
import indiana.cgl.hadoop.pagerank.helper.CreateGraphReduce;

import java.io.BufferedWriter;
		
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
		
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class HadoopPageRank extends Configured implements Tool{
 
	public static void main(String[] args) throws Exception {

		System.out.println("*********************************************");
        System.out.println("*           Hadoop PageRank                 *");
        System.out.println("*********************************************");
		
		if (args.length != 4) {
			String errorReport = "Usage:: \n"
					+ "hadoop jar HadoopPageRank.jar "
					+ "[inputDir][outputDir][numUrls][maximum loop count]\n";
			
			System.out.println(errorReport);
			System.exit(-1);
		}			

		String inputDir = args[0];
		String outputDir = args[1];
		int numUrls = Integer.parseInt(args[2]);
		int noIterations = Integer.parseInt(args[3]);
		int outputIndex = 0;
		
		long startTime = System.currentTimeMillis();
		
		Configuration config = new Configuration();
		config.setInt("numUrls", numUrls);
		System.out.println("Hadoop CreateGraph starts...\n");
		/////////////////////////////////////////////////////////////
		//convert elements in the adjacency matrix format into (key, value) pairs  
		Job job1 = new Job(config, "CreateGraph");
		FileSystem fs = FileSystem.get(config);
		
		job1.setJarByClass(HadoopPageRank.class);
		job1.setMapperClass(CreateGraphMap.class);
		job1.setReducerClass(CreateGraphReduce.class);
		job1.setOutputKeyClass(LongWritable.class);
		job1.setOutputValueClass(Text.class);
		
		FileInputFormat.setInputPaths(job1, new Path(inputDir));
		if (fs.exists(new Path(String.valueOf(outputIndex))))
			fs.delete(new Path(String.valueOf(outputIndex)), true);
		FileOutputFormat.setOutputPath(job1, new Path(String.valueOf(outputIndex)));
		
		int numReduceTasks = 1;
		job1.setNumReduceTasks(numReduceTasks);
		
		job1.waitForCompletion(true);
		if (!job1.isSuccessful()){
			System.out.println("Hadoop CreateGraph failed, exit...");
			System.exit(-1);
		}
		
		System.out.println("Hadoop PageRank starts...\n");
		/////////////////////////////////////////////////////
		//core computation that require multiple iterations to make rank values results converge
		for (int i=0;i<noIterations;i++){
			System.out.println("Hadoop PageRank iteration "+ i +"...\n");
			Job job2 = new Job(config, "HadoopPageRank");
			//config.setInt("numUrls", numUrls);
			job2.setJarByClass(HadoopPageRank.class);
			job2.setMapperClass(PageRankMap.class);
			job2.setReducerClass(PageRankReduce.class);
			job2.setOutputKeyClass(LongWritable.class);
			job2.setOutputValueClass(Text.class);
			
			//the output in the current iteration will become input in next iteration.
			FileInputFormat.setInputPaths(job2, new Path(String.valueOf(outputIndex)));
			FileOutputFormat.setOutputPath(job2, new Path(String.valueOf(outputIndex+1)));
			
			numReduceTasks = 1;
			job2.setNumReduceTasks(numReduceTasks);
			
			job2.waitForCompletion(true);
			if (!job2.isSuccessful()){
				System.out.format("Hadoop PageRank iteration:{"+ i +"} failed, exit...", i);
				System.exit(-1);
			}
			//clean the intermediate data directories.
			fs.delete(new Path(String.valueOf(outputIndex)), true);
			outputIndex++;
		}
		
		System.out.println("Hadoop CleanUptResults starts...\n");
		/////////////////////////////////////////////////////
		//collect the (url_id,rank_value) tuple from output in stage 2 
		
		Job job3 = new Job(config, "CleanUptResults");

		job3.setJarByClass(HadoopPageRank.class);
		job3.setMapperClass(CleanupResultsMap.class);
		job3.setReducerClass(CleanupResultsReduce.class);
		job3.setOutputKeyClass(LongWritable.class);
		job3.setOutputValueClass(Text.class);
		
		FileInputFormat.setInputPaths(job3, new Path(String.valueOf(outputIndex)));
		FileOutputFormat.setOutputPath(job3, new Path(String.valueOf(outputDir)));
		
		numReduceTasks = 1;
		job3.setNumReduceTasks(numReduceTasks);
		
		job3.waitForCompletion(false);
		if (!job3.isSuccessful()){
			System.out.println("Hadoop CleanUptResults failed, exit...");
			System.exit(-1);
		}
		
		double executionTime = (System.currentTimeMillis() - startTime) / 1000.0;
		System.out.println("########################################################");
		System.out.println("#   Hadoop PageRank Job take " + executionTime + " sec.");
		System.out.println("########################################################");
		System.exit(0);
	}
	@Override
	public int run(String[] arg0) throws Exception {
		// TODO Auto-generated method stub
		return 0;
	}

}
