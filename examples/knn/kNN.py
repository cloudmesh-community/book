'''
Created on Sep 16, 2010
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

@author: pbharrin
'''
from numpy import *
import operator
from os import listdir

#	Use k Nearest Neighbors to classify inX accortding to existing dataSet with known ratings in labels
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]	# Number of entries in dataSet
    diffMat = tile(inX, (dataSetSize,1)) - dataSet	# 	Array of same shape as dataSet holding inX-dataSet entry in each position
    sqDiffMat = diffMat**2	# Square entries in diffMat
    sqDistances = sqDiffMat.sum(axis=1)	# Sum over vector components
    distances = sqDistances**0.5	# Traditional Euclidean distance foreach dataSet entry
    sortedDistIndicies = distances.argsort()	# argsort returns indices that sort distances     
    classCount={}	# An empty dictionary key:value pairs key = labels  value = number times this label in set of k       
    for i in range(k):	# Run over k nearest neighbors
        voteIlabel = labels[sortedDistIndicies[i]]	# Label of this neighbor
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1	# .get gets current count for voteIlabel and returns zero if first time voteIlabel seen (default = 0)
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)	# Sort classCount (highest to lowest) by voteIlabel count
    return sortedClassCount[0][0]	# The label that occurs most often in k nearest neighbors

#	Set up a datset of 4 (2D vector) items -- each of which has one of two labels
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

#	Read Rating Data set returning set of 1000 3 Vectors and numeric label
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

# Normalize vector components to be between 0 and 1 
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

# Use 90% data to predict other 10%. Print fraction of errors
def datingClassTest(hoRatio):
    # hoRatio is hold out percentage
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
#        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print "Number Bad %f" % errorCount

# Remove 2 files from original here

# Addition to generate file for 3D PLotting system PlotViz
def WritePlotViz(filename):
	PVFile = open(filename, 'w')
	datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
	normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
	for i in range(normMat.shape[0]):
		PVFile.write( "%d\t%f\t%f\t%f\t%d\n" %(i, normMat[i,0], normMat[i,1], normMat[i,2], datingLabels[i]) )