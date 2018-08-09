'''This file has code to perform k-means clustering for the data in sample.csv. Make sure to include sample.csv in the working directory'''
from pylab import plot,show
from numpy import array
from scipy.cluster.vq import kmeans,vq
import numpy as np
import matplotlib.pyplot as plt

# Loads a CSV files into an array.
# Numeric attributes are converted to floats, nominal attributes
# are represented with strings.
# Parameters:
# fileName: name of the CSV file to be read
# Returns: a list of tuples
def loadCSV(fileName):
    fileHandler = open(fileName, "rt")
    lines = fileHandler.readlines()
    fileHandler.close()
    del lines[0] # remove the header
    dataset = []
    for line in lines:
        instance = lineToTuple(line)
        instance = np.delete(instance,0,0)
        dataset.append(instance)
    return array(dataset,dtype=np.float32)

# Converts a comma separated string into a tuple
# Parameters
#   line: a string
# Returns: a tuple
def lineToTuple(line):
    cleanLine = line.strip()                  # remove leading/trailing whitespace and newlines
    cleanLine = cleanLine.replace('"', '')# get rid of quotes
    lineList = cleanLine.split(",")          # separate the fields
    stringsToNumbers(lineList)            # convert strings into numbers
    lineTuple = array(lineList)
    return lineTuple

# Destructively converts all the string elements representing numbers
# to floating point numbers.
# Parameters:
#   myList: a list of strings
# Returns None
def stringsToNumbers(myList):
    for i in range(len(myList)):
        if (isValidNumberString(myList[i])):
            myList[i] = float(myList[i])

# Checks if a given string can be safely converted into a positive float.
# Parameters:
#   s: the string to be checked
# Returns: True if the string represents a positive float, False otherwise
def isValidNumberString(s):
  if len(s) == 0:
    return False
  if len(s) > 1 and s[0] == "-":
    s = s[1:]
  for c in s:
    if c not in "0123456789.":
      return False
  return True

# data generation. Set file location here
data = loadCSV("sample.csv")

# computing K-Means with K = 2 (2 clusters)but you can change this. Plot works upto 5 clusters
K=5
centroids,_ = kmeans(data,K)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

# some plotting using numpy's logical indexing
plt.figure("Clustering K={0} T Shirts".format(K))
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or', data[idx==2,0],
     data[idx==2,1],'og', data[idx==3,0],data[idx==3,1],'oy', data[idx==4,0],data[idx==4,1],'om')
plot(centroids[:,0],centroids[:,1],'sk',markersize=8)
show()
