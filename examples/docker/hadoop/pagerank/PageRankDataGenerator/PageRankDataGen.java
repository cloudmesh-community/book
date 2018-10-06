import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
/*
 * @author Hui Li (lihui@indiana.edu)
 */

 public class PageRankDataGen{

 public static void main(String[] args) {

                System.out.println("*********************************************");
                System.out.println("* The part 1 of assignment#1 in B649 class  *");
                System.out.println("* PageRank input Data generator             *");
                System.out.println("*********************************************");

                if (args.length != 3) {
                        String error_report = "\nUsage: "
                        + "java PageRankDataGen "
                        + "[output file name][num of urls][num of groups]\n" 
                        + "e.g.: "                      
                        + "java PageRankDataGen pagerank.input.1000.groupid 1000 50";
                        System.out.println(error_report);               
                        System.exit(-1);                                
		}
		int numUrls = Integer.parseInt(args[1]);
		int numGroups = Integer.parseInt(args[2]);
		String fileNameBase = args[0];
	try{	
		for (int index=0; index<numGroups; index++){
			
		String fileName = fileNameBase + "."+index;
		BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
		String strLine = null;
		int i, j;

			/*
			 * simulate the power law distributions.
			 */

		StringBuffer strBuf = null;
		for (i = 0; i < numUrls; i++) {
			strBuf = new StringBuffer();
			strBuf.append(Integer.toString(i));
			for (j = 0; j < numUrls; j++) {
				if ((-3*i*i + 7 + i) % (j + 3) == 0)
					strBuf.append(" "+j);
			}// for j;
			strBuf.append("\n");
			writer.write(strBuf.toString());
		}//for i
			writer.flush();
			writer.close();
		}//for index
	} catch (IOException e) {
		e.printStackTrace();
	}
}//main
}
