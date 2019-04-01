'''Performs k-means using the implementation of k-means in scipy'''
from scipy.cluster.vq import kmeans,vq
import numpy as np
import matplotlib.pyplot as plt

Radii = np.array([ 0.375, 0.55, 0.6, 0.25 ])

nClusters = 4
nRepeat = 250
tot = nClusters*nRepeat
Centers1 = np.tile([0,0], (nRepeat,1))
Centers2 = np.tile([3,3], (nRepeat,1))
Centers3 = np.tile([0,3], (nRepeat,1))
Centers4 = np.tile([3,0], (nRepeat,1))
Centers = np.concatenate((Centers1, Centers2, Centers3, Centers4))
xvalues1 =  np.tile(Radii[0], nRepeat)
xvalues2 =  np.tile(Radii[1], nRepeat)
xvalues3 =  np.tile(Radii[2], nRepeat)
xvalues4 =  np.tile(Radii[3], nRepeat)
Totradii = np.concatenate((xvalues1, xvalues2, xvalues3, xvalues4))
xrandom = np.random.randn(tot)
xrange = xrandom * Totradii
yrandom = np.random.randn(tot)
yrange = yrandom * Totradii
Points = np.column_stack((xrange, yrange))
data = Points + Centers

# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(data,2)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

# some plotting using numpy's logical indexing
plt.figure("Clustering K=2 Large Radius")
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()


# computing K-Means with K = 4 (4 clusters)
centroids4,_ = kmeans(data,4)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

# some plotting using numpy's logical indexing
plt.figure("Clustering K=4 Large Radius")
plt.plot(data[idx4==0,0],data[idx4==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx4==1,0],data[idx4==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx4==2,0],data[idx4==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx4==3,0],data[idx4==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(centroids4[:,0],centroids4[:,1],'sg',markersize=8)
plt.show()

Radii = 0.25*Radii
xvalues1 =  np.tile(Radii[0], nRepeat)
xvalues2 =  np.tile(Radii[1], nRepeat)
xvalues3 =  np.tile(Radii[2], nRepeat)
xvalues4 =  np.tile(Radii[3], nRepeat)
Totradii = np.concatenate((xvalues1, xvalues2, xvalues3, xvalues4))
xrandom = np.random.randn(tot)
xrange = xrandom * Totradii
yrandom = np.random.randn(tot)
yrange = yrandom * Totradii
Points = np.column_stack((xrange, yrange))
data = Points + Centers

# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(data,2)
# assign each sample to a cluster
idx,_ = vq(data,centroids)


# some plotting using numpy's logical indexing
plt.figure("Clustering K=2 Small Radius")
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()


# computing K-Means with K = 4 (4 clusters)
centroids4,_ = kmeans(data,4)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

# some plotting using numpy's logical indexing
plt.figure("Clustering K=4 Small Radius")
plt.plot(data[idx4==0,0],data[idx4==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx4==1,0],data[idx4==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx4==2,0],data[idx4==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx4==3,0],data[idx4==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(centroids4[:,0],centroids4[:,1],'sg',markersize=8)
plt.show()

Radii = 6*Radii
xvalues1 =  np.tile(Radii[0], nRepeat)
xvalues2 =  np.tile(Radii[1], nRepeat)
xvalues3 =  np.tile(Radii[2], nRepeat)
xvalues4 =  np.tile(Radii[3], nRepeat)
Totradii = np.concatenate((xvalues1, xvalues2, xvalues3, xvalues4))
xrandom = np.random.randn(tot)
xrange = xrandom * Totradii
yrandom = np.random.randn(tot)
yrange = yrandom * Totradii
Points = np.column_stack((xrange, yrange))
data = Points + Centers

# computing K-Means with K = 2 (2 Very Large clusters)
centroids,_ = kmeans(data,2)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

# some plotting using numpy's logical indexing
plt.figure("Clustering K=2 Very Large Radius")
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()


# computing K-Means with K = 4 (4 Very Large clusters)
centroids4,_ = kmeans(data,4)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

# some plotting using numpy's logical indexing
plt.figure("Clustering K=4 Very Large Radius")
plt.plot(data[idx4==0,0],data[idx4==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx4==1,0],data[idx4==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx4==2,0],data[idx4==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx4==3,0],data[idx4==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(centroids4[:,0],centroids4[:,1],'sg',markersize=8)
plt.show()