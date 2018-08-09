'''This file gets the page rank according to google page rank.'''
#!/usr/bin/env python
# Google Pagerank Checksum Algorithm (Firefox Toolbar)
# Downloaded from http://pagerank.phurix.net/
# Requires: Python >= 2.4 
# Versions:
# pagerank2.py 0.2 - Fixed a minor formatting bug
# pagerank2.py 0.1 - Public release
# Settings


import httplib

prhost='toolbarqueries.google.com'                                     #define the host      
prpath='/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s'       #define the path with 2 blanks(indicated by %s). These are for the hash of the query and the query respectively
 
# Function definitions
#The hash function which computes the hash for the query. Do not change this function
def GetHash (query):
    SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE."      
    Result = 0x01020345
    for i in range(len(query)) :
        Result ^= ord(SEED[i%len(SEED)]) ^ ord(query[i])
        Result = Result >> 23 | Result << 9
        Result &= 0xffffffff
    return '8%x' % Result

'''This method makes http requests and recieves response regarding the page rank'''
def GetPageRank (query):
    conn = httplib.HTTPConnection(prhost)                               #make connection to the host
    hash = GetHash(query)                                               #compute hash of the query using the hash function
    path = prpath % (hash,query)                                        #add the hash and actual query to the path.
    conn.request("GET", path)                                           #request
    response = conn.getresponse()                                       #response
    data = response.read()                                              #read data
    conn.close()                                                        #close connection
    return data.split(":")[-1]                              
    
'''Prints the query and the page rank obtained using the GetPageRank().'''
def PrintPageRank (query):
	print query, " PageRank ", GetPageRank(query)
	return
 
PrintPageRank("http://en.wikipedia.org")
PrintPageRank("http://www.soic.indiana.edu")
PrintPageRank("http://www.infomall.org")



