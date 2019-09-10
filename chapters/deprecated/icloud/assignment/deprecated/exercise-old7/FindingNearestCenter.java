private void findNearestCenter(ArrTable<DoubleArray> cenTable, ArrTable<DoubleArray> previousCenTable, ArrayList<DoubleArray> dataPoints) {
	double err = 0;
	for (DoubleArray aPoint : dataPoints) {
		//for each data point, find the nearest centroid
		double minDist = -1;
		double tempDist = 0;
		int nearestPartitionID = -1; // Keeps track of the nearest center ID
		for (ArrPartition ap : previousCenTable.getPartitions()) {
			DoubleArray aCentroid = (DoubleArray) ap.getArray();
			/* TODO – Write code here */
			tempDist = // this is the Euclidean distance between aPoint and aCentroid. Use Utils.calcEucDistSquare() for this

			// Next check if tempDist is smaller than current minDist (unless it’s -1)
			// If so, set the minDist to tempDist and mark the current center ID as the nearest center found so far. To get the center ID use the ap.getPartitionID() method.
		}
		err += minDist;

		//for the certain data point, found the nearest centroid.
		// add the data to a new cenTable.
		double[] partial = new double[vectorSize + 1];
		for (int j = 0;j < vectorSize;j++) {
         	partial[j] = aPoint.getArray()[j];
      	}
      	partial[vectorSize] = 1;
      
      	if (cenTable.getPartition(nearestPartitionID) == null) {
         	ArrPartition<DoubleArray> tmpAp = new ArrPartition<DoubleArray>(nearestPartitionID, new DoubleArray(partial, 0, vectorSize + 1));
         	cenTable.addPartition(tmpAp);
      	}
      	else {
          	ArrPartition<DoubleArray> apInCenTable = cenTable.getPartition(nearestPartitionID);
          	for (int i = 0;i < vectorSize + 1;i++) {
             	apInCenTable.getArray().getArray()[i] += partial[i];
          	}
      	}
    }
 	System.out.println("Errors: " + err);
}