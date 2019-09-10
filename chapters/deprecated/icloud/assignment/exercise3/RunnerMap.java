/*file: RunnerMap.java*/
package cgl.hadoop.apps.runner;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/**
 * @author Thilina Gunarathne (tgunarat@cs.indiana.edu)
 * 
 * @editor Stephen, TAK-LON WU (taklwu@indiana.edu)
 */

public class RunnerMap extends Mapper<String, String, IntWritable, Text> {
  
	private String localDB = "";
	private String localBlastProgram = "";

    
	@Override
	public void setup(Context context) throws IOException{
		Configuration conf = context.getConfiguration();
		Path[] local = DistributedCache.getLocalCacheArchives(conf);
		
		/* Write your code here
    		   get two absolute filepath for localDB and localBlastBinary
    		*/
	
	}
	

	public void map(String key, String value, Context context) throws IOException,
		InterruptedException {
		
		long startTime = System.currentTimeMillis();
		String endTime = "";
		
		Configuration conf = context.getConfiguration();
		String programDir = conf.get(DataAnalysis.PROGRAM_DIR);
		String execName = conf.get(DataAnalysis.EXECUTABLE);
		String cmdArgs = conf.get(DataAnalysis.PARAMETERS);
		String outputDir = conf.get(DataAnalysis.OUTPUT_DIR);
		String workingDir = conf.get(DataAnalysis.WORKING_DIR);
		
    	String localInputFile = null;
   	 	String outFile = null;
    	String stdOutFile = null;
  		String stdErrFile = null;
		
		System.out.println("the map key : " + key);
		System.out.println("the value path : " + value.toString());
		System.out.println("Local DB : " + this.localDB);

		    /*
		      Write your code to get localInputFile, outFile, 
		      stdOutFile and stdErrFile
		    */
    
 
		// Prepare the arguments to the executable
		String execCommand = cmdArgs.replaceAll("#_INPUTFILE_#", localInputFile);
		if (cmdArgs.indexOf("#_OUTPUTFILE_#") > -1) {
			execCommand = execCommand.replaceAll("#_OUTPUTFILE_#", outFile);
		}else{
			outFile = stdOutFile;
		}
		
		endTime = Double.toString(((System.currentTimeMillis() - startTime) / 1000.0));
		System.out.println("Before running the executable Finished in " + endTime + " seconds");
		
		execCommand = this.localBlastProgram + File.separator + execName 
		+ " " + execCommand + " -db " + this.localDB;
		//Create the external process
		
		startTime = System.currentTimeMillis();
		
		Process p = Runtime.getRuntime().exec(execCommand);
 
		OutputHandler inputStream = new OutputHandler(p.getInputStream(), "INPUT", stdOutFile);
		OutputHandler errorStream = new OutputHandler(p.getErrorStream(), "ERROR", stdErrFile);
 
		// start the stream threads.
		inputStream.start();
		errorStream.start();
		
		p.waitFor();
		//end time of this procress
		endTime = Double.toString(((System.currentTimeMillis() - startTime) / 1000.0));
		System.out.println("Program Finished in " + endTime + " seconds");
		
		//Upload the results to HDFS
		startTime = System.currentTimeMillis();
		
		Path outputDirPath = new Path(outputDir);
		Path outputFileName = new Path(outputDirPath,fileNameOnly);
		fs.copyFromLocalFile(new Path(outFile),outputFileName);
 
		endTime = Double.toString(((System.currentTimeMillis() - startTime) / 1000.0));
		System.out.println("Upload Result Finished in " + endTime + " seconds");
		
	}
}
