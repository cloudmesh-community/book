public static void searchKeyword(String keyword) throws Exception {
	Configuration hbaseConfig = HBaseConfiguration.create();
	HTable dataTable = new HTable(hbaseConfig, Constants.CW09_DATA_TABLE_BYTES);
	HTable indexTable = new HTable(hbaseConfig, Constants.CW09_INDEX_TABLE_BYTES);
	HTable prTable = new HTable(hbaseConfig, Constants.CW09_PAGERANK_TABLE_BYTES);
		
	int topCount = 20;
	// this is the heap for storing the top 20 ranked pages
	PriorityQueue<PageRecord> topPages = new PriorityQueue<PageRecord>(topCount);
		
	// get the inverted index row with the given keyword
	keyword = keyword.toLowerCase();
    byte[] keywordBytes = Bytes.toBytes(keyword);
	Get gIndex = new Get(keywordBytes);
    Result indexRow = indexTable.get(gIndex);
		
    // loop through the document IDs in the row. Recall the schema of the clueWeb09IndexTable:
    // row key: term (keyword), column family: "frequencies", qualifier: document ID, cell value: term frequency in the corresponding document
	int pageCount = 0;
    for (KeyValue kv : indexRow.list()) {
        String pageDocId = null;
        int freq = 0;
        String pageUri = null;
        float pageRank = 0;

	    // Write your codes for the main part of implementation here
        // Step 1: get the document ID of one page, as well as the keyword's frequency in that page
		// Step 2: get the URI of the page from clueWeb09DataTable
		// Step 3: get the page rank value of this page from clueWeb09PageRankTable
	    // End of your code
            
        // Use the heap to select the top 20 pages according to page rank
	    PageRecord page = new PageRecord(pageDocId, pageUri, pageRank, freq);
	    if (topPages.size() < topCount) {
			topPages.offer(page);
	    }
	    else {
			PageRecord head = topPages.peek();
			if (page.pageRank > head.pageRank) {
				topPages.poll();
				topPages.offer(page);
			}
	    }
			
	    pageCount++;
	    if (pageCount % 100 == 0) {
			System.out.println("Evaluated " + pageCount + " pages.");
	    }
	}
    System.out.println("Evaluated " + pageCount + " pages.");
	dataTable.close();
	indexTable.close();
	prTable.close();
		
	System.out.println("Evaluated " + pageCount + " pages in total. Here are the top 20 pages according to page ranks:");
	Stack<PageRecord> stack = new Stack<PageRecord>();
	while (topPages.size() > 0) {
		stack.push(topPages.poll());
	}
	while (stack.size() > 0) {
		PageRecord page = stack.pop();
		System.out.println("Document ID: " + page.docId + ", URI: " + page.URI + ", page rank: " + page.pageRank + ", word frequency: "
			+ page.termFreq);
	}
}
