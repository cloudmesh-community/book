private void updateCenters(ArrTable<DoubleArray> cenTable) {
	for (ArrPartition<DoubleArray> partialCenTable : cenTable.getPartitions()) {
		double[] doubles = partialCenTable.getArray().getArray();
		/* TODO – Write code here */
		// Go through the components of the vector (i.e. a for loop) and divide it by the number of points assigned to that center.
		// The number of points can be found at doubles[vectorSize]
		// Vector components (x,y,z, etc.) can be found through 0 to (vectorSize – 1) indices in the doubles array


		doubles[vectorSize] = 0;
	}
	System.out.println("after calculate new centroids");
	Utils.printArrTable(cenTable);
}