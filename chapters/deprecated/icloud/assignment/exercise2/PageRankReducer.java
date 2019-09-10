/*file: PageRankReducer.java*/
package indiana.cgl.hadoop.pagerank;

import java.io.BufferedWriter;
/* see detail in source code */
 
public class PageRankReduce extends Reducer<LongWritable, Text, LongWritable, Text>{
  public void reduce(LongWritable key, Iterable<Text> values,
      Context context) throws IOException, InterruptedException {
    double sumOfRankValues = 0.0;
    String targetUrlsList = "";
    
    int sourceUrl = (int)key.get();
    int numUrls = context.getConfiguration().getInt("numUrls",1);
    
    //hint: each tuple may include rank value tuple or link relation tuple  
    for (Text value: values){
      String[] strArray = value.toString().split("#");
        /*Write your code here*/
    }
               // calculate using the formula
    sumOfRankValues = 0.85*sumOfRankValues+0.15*(1.0)/(double)numUrls; 
    context.write(key, new Text(sumOfRankValues+targetUrlsList));
  }
}
