package exercise;

import java.io.IOException;
import java.util.Iterator;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MinMaxAvgStd {
	
	public static class Map extends Mapper<LongWritable, Text, Text, Text> {
		public void map(LongWritable key, Text value, Context context) 
								throws IOException, InterruptedException {
			double min = 1, max = 0;
			double sumOfTerms = 0;
			double squareOfTerms = 0;
			int numberOfTerms = 0;
			
			StringTokenizer stringTokenizer = new StringTokenizer(value.toString());
			while (stringTokenizer.hasMoreTokens()) {
				double inputTerm = Double.parseDouble(value.toString());
				
				if (inputTerm > max)
					max = inputTerm;
				if (inputTerm < min)
					min = inputTerm;
				sumOfTerms+= inputTerm;
				squareOfTerms+= inputTerm * inputTerm;
				numberOfTerms++;
				
				context.write(new Text("Min:"), new Text(Double.toString(min)));
				context.write(new Text("Max:"), new Text(Double.toString(max)));
				context.write(new Text("properties"), new Text(Double.toString(sumOfTerms)
															+ " " + Double.toString(squareOfTerms)
															+ " " + Double.toString(numberOfTerms)));
				stringTokenizer.nextToken();
			}
		}
	}
	
	public static class Reduce extends Reducer<Text, Text, Text, DoubleWritable> {
		public void reduce(Text key, Iterable<Text> values, Context context)
								throws IOException, InterruptedException {
			double min = Double.MAX_VALUE, max = Double.MIN_VALUE;
			double sumOfTerms = 0, squareOfTerms = 0, average = 0, standardDeviation = 0;
			int numberOfTerms = 0;
			Iterator<Text> iterator = values.iterator();
			if (key.equals(new Text("Max:"))) {
				while (iterator.hasNext()) {
					double maxValue = Double.parseDouble(iterator.next().toString());
					max = Math.max(max, maxValue);
				}
				System.out.println("Final MAX is: " + max);
				context.write(key, new DoubleWritable(max));
			}
			else if (key.equals(new Text("Min:"))) {
				while (iterator.hasNext()) {
					double minValue = Double.parseDouble(iterator.next().toString());
					min = Math.min(min, minValue);
				}
				System.out.println("Final MIN is: " + min);
				context.write(key, new DoubleWritable(min));
			}
			else if (key.equals(new Text("properties"))) {
				while (iterator.hasNext()) {
					String properties[] = iterator.next().toString().split(" ");
					sumOfTerms += Double.parseDouble(properties[0]);
					squareOfTerms += Double.parseDouble(properties[1]);
					numberOfTerms += Double.parseDouble(properties[2]);
				}
				System.out.println("Number of terms are: " + numberOfTerms);
				average = sumOfTerms/numberOfTerms;
				System.out.println("Average is: " + average);
				context.write(new Text("Avg:"), new DoubleWritable(average));
				standardDeviation = Math.sqrt((squareOfTerms/numberOfTerms) - (average * average));
				System.out.println("Standard Deviation is: " + standardDeviation);
				context.write(new Text("Std:"), new DoubleWritable(standardDeviation));
			}	
		}
	}
	
	public static void main(String args[]) throws Exception {
		Configuration configuration = new Configuration();
		String otherArgs[] = new GenericOptionsParser(configuration, args).getRemainingArgs();
		if (otherArgs.length != 2) {
			System.err.println("Usage: MinMaxAvgStd <in> <out>");
		    System.exit(2);
		}
		
		Job job = new Job(configuration, "minMaxOpns");
		job.setJarByClass(MinMaxAvgStd.class);
		job.setMapperClass(Map.class);
		job.setReducerClass(Reduce.class);
		
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(DoubleWritable.class);
		
		FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
		
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}

