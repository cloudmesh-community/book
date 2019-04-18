package indiana.cgl.hadoop.pagerank.helper;

import java.io.IOException;
 
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer.Context;
import org.apache.hadoop.mapreduce.Reducer;

public class CleanupResultsReduce extends Reducer<LongWritable, Text, LongWritable, Text>{
public void reduce(LongWritable key, Iterable<Text> values,
		Context context) throws IOException, InterruptedException {
	context.write(key, values.iterator().next());
}
}