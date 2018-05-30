public static class FibMapper extends TableMapper<ImmutableBytesWritable, Writable> {		
	@Override
	protected void map(ImmutableBytesWritable rowKey, Result result, Context context) throws IOException, InterruptedException {
		byte[] docIdBytes = rowKey.get();
		byte[] contentBytes = result.getValue(Constants.CF_DETAILS_BYTES, Constants.QUAL_CONTENT_BYTES);
		String content = Bytes.toString(contentBytes);
			
		// TODO: write your implementation for getting the term frequencies from each document, 
		// and generating Put objects for clueWeb09IndexTable. 
            	// Hint: use the "getTermFreqs" function to count the frequencies of terms in content.
            	// The schema of the clueWeb09IndexTable is:
            	// row key: term, column family: "frequencies", qualifier: document Id, cell value: term frequency in the corresponding document
            	// Check iu.pti.hbaseapp.Constants for useful constant values.


	}
}