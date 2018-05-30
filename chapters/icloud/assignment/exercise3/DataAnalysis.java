/*file: DataAnalysis.java*/
package cgl.hadoop.apps.runner;
 
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
 
import cgl.hadoop.apps.DataFileInputFormat;
import java.net.URI;
 
public class DataAnalysis extends Configured implements Tool {
 
  public static String WORKING_DIR = "working_dir";
	public static String OUTPUT_DIR = "out_dir";
	public static String EXECUTABLE = "exec_name";
	public static String PROGRAM_DIR = "exec_dir";
	public static String PARAMETERS = "params";
	public static String DB_NAME = "nr";
	public static String DB_ARCHIVE = "BlastDB.tar.gz";
 
/**
 * Launch the MapReduce computation.
 * This method first, remove any previous working directories and create a new one
 * Then the data (file names) is copied to this new directory and launch the 
 * MapReduce (map-only though) computation.
 * @param numMapTasks - Number of map tasks.
 * @param numReduceTasks - Number of reduce tasks =0.
 * @param programDir - The directory where the Cap3 program is.
 * @param execName - Name of the executable.
 * @param dataDir - Directory where the data is located.
 * @param outputDir - Output directory to place the output.
 * @param cmdArgs - These are the command line arguments to the Cap3 program.
 * @throws Exception - Throws any exception occurs in this program.
 */
	void launch(int numReduceTasks, String programDir,
			String execName, String workingDir, String databaseArchive, String databaseName, 
			String dataDir, String outputDir, String cmdArgs) throws Exception {
 
		Configuration conf = new Configuration();
		Job job = new Job(conf, execName);
 
		// First get the file system handler, delete any previous files, add the
		// files and write the data to it, then pass its name as a parameter to
		// job
		Path hdMainDir = new Path(outputDir);
		FileSystem fs = FileSystem.get(conf);
		fs.delete(hdMainDir, true);
 
		Path hdOutDir = new Path(hdMainDir, "out");
 
		// Starting the data analysis.
		Configuration jc = job.getConfiguration();
 
		jc.set(WORKING_DIR, workingDir);
		jc.set(EXECUTABLE, execName);
		jc.set(PROGRAM_DIR, programDir); // this the name of the executable archive
		jc.set(DB_ARCHIVE, databaseArchive);
		jc.set(DB_NAME, databaseName);
		jc.set(PARAMETERS, cmdArgs);
		jc.set(OUTPUT_DIR, outputDir);
		
 
		long startTime = System.currentTimeMillis();
		DistributedCache.addCacheArchive(new URI(programDir), jc);
		System.out.println("Add Distributed Cache in "
				+ (System.currentTimeMillis() - startTime) / 1000.0
				+ " seconds");		
		
 
		FileInputFormat.setInputPaths(job, dataDir);
		FileOutputFormat.setOutputPath(job, hdOutDir);
 
		job.setJarByClass(DataAnalysis.class);
		job.setMapperClass(RunnerMap.class);
		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(Text.class);
		
		job.setInputFormatClass(DataFileInputFormat.class);
		job.setOutputFormatClass(SequenceFileOutputFormat.class);
		job.setNumReduceTasks(numReduceTasks);
		
		startTime = System.currentTimeMillis();
 
		int exitStatus = job.waitForCompletion(true) ? 0 : 1;
		System.out.println("Job Finished in "
				+ (System.currentTimeMillis() - startTime) / 1000.0
				+ " seconds");
		//clean the cache
 
		
		System.exit(exitStatus);
	}
 
	public int run(String[] args) throws Exception {
		if (args.length < 8) {
			System.err.println("Usage: DataAnalysis <Executable and Database Archive on HDFS>
			 <Executable> <Working_Dir> <Database dir under archive> <Database name>
			  <HDFS_Input_dir> <HDFS_Output_dir> <Cmd_args>");
			ToolRunner.printGenericCommandUsage(System.err);
			return -1;
		}
		String programDir = args[0];
		String execName = args[1];
		String workingDir = args[2];
		String databaseArchive = args[3];
		String databaseName = args[4];
		String inputDir = args[5];
		String outputDir = args[6];
		//"#_INPUTFILE_# -p 95 -o 49 -t 100"
		String cmdArgs = args[7] ;
		
		int numReduceTasks = 0;// We don't need reduce here.
 
		launch(numReduceTasks, programDir, execName, workingDir , 
			databaseArchive, databaseName,inputDir,	outputDir, cmdArgs);
		return 0;
	}
 
	public static void main(String[] argv) throws Exception {
		int res = ToolRunner.run(new Configuration(), new DataAnalysis(), argv);
		System.exit(res);
	}
}
