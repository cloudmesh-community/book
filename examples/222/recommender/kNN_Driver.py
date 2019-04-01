'''A wrapper around kNN.py. Include the kNN.py and datingTestSet2 in the current working directory'''

import kNN                                                             #importing the methods and variables from kNN.py. these methods/variables can be accessed as kNN.MethodName() or kNN.variableName
import matplotlib.pyplot as plt
import numpy as np


FigDating = plt.figure()

group,labels = kNN.createDataSet()                                       #Create the data set with four items(2-D vectors). Each of them one of two labels associated with them 
colormap1 = { 'A':'red', 'B':'blue'}                                     #Make a color map
ColoredGroupLabels = []

for things in labels:                                                   #Get a vector representing the colors 
    ColoredGroupLabels.append(colormap1[things])                         #for each data item

ax1 = FigDating.add_subplot(311, xlim=(-0.1,1.1), ylim=(-.05,1.15))     #Dividing the figure into 3 sub plots and selecting the top-most
ax1.scatter(group[:,0], group[:,1], s= 20, c= ColoredGroupLabels, marker = 'o' )    #Plotting the data as a scatter plot with color(c) property as per the labelling. 

#Testing with new points
testvector = [.2, .2]                                                   #first point 
answer = kNN.classify0(testvector,group, labels, 3)                     #classify the first point
# type "print answer" to see result
ax1.scatter(testvector[0], testvector[1], s= 20, c= colormap1[answer], marker = 'x' ) #plot first point
#second point -  created, classified and plotted
testvector = [.5, .5]                                                   
answer = kNN.classify0(testvector,group, labels, 3)
ax1.scatter(testvector[0], testvector[1], s= 20, c= colormap1[answer], marker = 'x' )
#third point -  created, classified and plotted
testvector = [.75, .75]
answer = kNN.classify0(testvector,group, labels, 3)
ax1.scatter(testvector[0], testvector[1], s= 20, c= colormap1[answer], marker = 'x' )

'''Perform K-Nearest Neighbor classification on the datingTestSet2 data set. Do not forget to include the data set in the working directory'''
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')                          # Load data values and labels from the datingTestSet2.txt
datingLabelArray = np.array(datingLabels)                                                   

colormap2 = { 1:'red', 2:'blue', 3:'green' }                                                    #Define color map with 3 colors

ColoredDatingLabel = [] 
for things in datingLabelArray:                                                                     #Get a vector representing the colors
    ColoredDatingLabel.append(colormap2[things])                                                    #for each data item

ax2 = FigDating.add_subplot(312, xlim=(0,100000), ylim=(0,25))                                      #create second sub plot 
ax2.scatter(datingDataMat[:,0], datingDataMat[:,1], s= 20, c= ColoredDatingLabel, marker = 'o' )    #Plot a scatter diagram for the data loaded

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)                                              #normalize the data
ax3 = FigDating.add_subplot(313, xlim=(0,1), ylim=(0,1))                                            #create third sub plot
ax3.scatter(normMat[:,0], normMat[:,1], s = 20, c= ColoredDatingLabel, marker = 'o' )               #Plot normalized data

plt.show()

NumberBad = kNN.datingClassTest(0.1) 