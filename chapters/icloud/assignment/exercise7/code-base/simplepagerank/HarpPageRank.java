package edu.iu.simplepagerank;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import edu.iu.fileformat.MultiFileInputFormat;


public class HarpPageRank {
	public static void main(String[] args) throws Exception {
		 Configuration conf = new Configuration();
		 
		 System.out.println("*********************************************");
	     System.out.println("*           Harp PageRank                 *");
	     System.out.println("*********************************************");
			
		 
		 String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		    		
		 if (args.length != 4) {
				String Usage = "Usage:: \n"
						+ "hadoop jar HarpPageRank.jar "
						+ "[inputDir][outputDir][numUrls][maximum loop count]\n";
				System.out.println(Usage);
				System.exit(-1);
		}		
		    
		String inputDir = args[0];
		String outputDir = args[1];
		int numUrls = Integer.parseInt(args[2]);
		int noIterations = Integer.parseInt(args[3]);
		
		Path outputPath = new Path(outputDir);
		FileSystem fs = FileSystem.get(conf);
		if (fs.exists(outputPath)) {
			fs.delete(outputPath, true);
		}
		

		conf.setInt(PageRankConstants.NUM_ITERATONS, noIterations);
		conf.setInt(PageRankConstants.NUM_URLS, numUrls);
		
		Job job =  Job.getInstance(conf, "harp page rank");
	    JobConf jobConf = (JobConf) job.getConfiguration();
	    jobConf.set("mapreduce.framework.name", "map-collective");
	    jobConf.setNumReduceTasks(0);
	    job.setJarByClass(HarpPageRank.class);
	    job.setMapperClass(PageRankMapper.class);
	    job.setInputFormatClass(MultiFileInputFormat.class);
	    job.setOutputKeyClass(LongWritable.class);
	    job.setOutputValueClass(Text.class);
	    FileInputFormat.addInputPath(job, new Path(inputDir));
	    FileOutputFormat.setOutputPath(job, new Path(outputDir));
	    System.exit(job.waitForCompletion(true) ? 0: 1);
	    
	    
	}
}
