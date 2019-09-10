public void computePartialPR(Map<Long, ArrayList<Long>> partialGraph, Long2DoubleKVTable localPRTable, Long2DoubleKVTable globalPRTable){
        
        for (Entry<Long, ArrayList<Long>> entry : partialGraph.entrySet()) {
            Long sourceUrl = entry.getKey();
            ArrayList<Long> targetUrls = entry.getValue();
            System.out.println("sourceURL: "+sourceUrl);
            if(targetUrls == null ){
                // simply assume that the IDs of pages are: 0,1,2,...,(numUrls-1)
                System.out.println("targetUrls is null");
                double pr = localPRTable.getVal(sourceUrl) / numUrls;
                // TODO - Students write Code here
                // Add pr to the page rank of all other URLs in globalPRTable
                // Note. The addKeyVal(key, val) method in globalPRTable will
                // automatically sum values if the key exists. If the key does
                // NOT exist then a new entry will be made.
               

            }else{
                int numOfOutLinks = targetUrls.size();
                double pr = localPRTable.getVal(sourceUrl) / numOfOutLinks;
                // TODO - Students write Code here
                // Add pr to the page rank of all target URLs.
               
               
                
            }
        }
    }