package indiana.cgl.hadoop.pagerank;

import java.util.ArrayList;

public class RankRecord {
	public int sourceUrl;
	public double rankValue;
	public ArrayList<Integer> targetUrlsList;
	
	public RankRecord(String strLine){
		String[] strArray = strLine.split("#");
		sourceUrl = Integer.parseInt(strArray[0].split("\t")[0]);
		rankValue = Double.parseDouble(strArray[0].split("\t")[1]);
		targetUrlsList = new ArrayList<Integer>();
		for (int i=1;i<strArray.length;i++){
			targetUrlsList.add(Integer.parseInt(strArray[i]));
		}
	}
}
