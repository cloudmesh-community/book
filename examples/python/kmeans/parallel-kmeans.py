'''This file has code to perform kmeans in a parallel fashion. If the parellism parameters is set = 2 it k-means is parallelized If it is set to 1 it is not.'''
from scipy.cluster.vq import vq
import numpy as np
import matplotlib.pyplot as plt
    
def kmeans_gcf(obs, NumClust, iter=20, thresh=1e-5, Parallelism = 1, MaxMean = 1):
	if int(iter) < 1:
		raise ValueError('iter must be at least 1.')
	#initialize best distance value to a large value
        best_dist = np.inf
        if NumClust < 1:
            raise ValueError("Asked for 0 cluster ? ")
            
        for i in range(iter):
            #the intial code book is randomly selected from observations
            book, distortavg, distortmax = raw_kmeans_gcf(obs, NumClust, thresh, Parallelism)
            dist = distortavg
            if MaxMean == 2:
            	dist = distortmax
            if dist < best_dist:
                best_book = book
                best_dist = dist
	return best_book, best_dist

def raw_kmeans_gcf(obs, NumClust, thresh=1e-5, Parallelism = 1):
	""" "raw" version of k-means.

	Returns
	-------
	code_book :
	the lowest distortion codebook found.
	avg_dist :
	the average distance a observation is from a code in the book.
	Lower means the code_book matches the data better.

	See Also
	--------
	kmeans : wrapper around k-means

	XXX should have an axis variable here.

	Examples
	--------
	Note: not whitened in this example.

	>>> from numpy import array
	>>> from scipy.cluster.vq import _kmeans
	>>> features  = array([[ 1.9,2.3],
	...                    [ 1.5,2.5],
	...                    [ 0.8,0.6],
	...                    [ 0.4,1.8],
	...                    [ 1.0,1.0]])
	>>> book = array((features[0],features[2]))
	>>> _kmeans(features,book)
	(array([[ 1.7       ,  2.4       ],
	   [ 0.73333333,  1.13333333]]), 0.40563916697728591)

	"""
	
	#	Initialize Code Book
	No = obs.shape[0]
	code_book = np.take(obs, np.random.randint(0, No, NumClust), 0)
	# obs is data; No is Number of Datapoints gotten from size of obs; NumClust is number of clusters desired
	# randinit(I1, I2, Num) calculates Num random integers r I1 <= r < I2
	# take returns an array selected from obs with 0'th index (lat argument specifies dimension) given in list of indices returned by randint
	#
	Iseven = np.empty([tot], dtype=bool)
	for i in np.arange(tot):
		Iseven[i] = (i%2 == 0);
	obs1 = np.compress(Iseven, obs, 0)
	obs2 = np.compress(np.logical_not(Iseven), obs, 0)

	avg_dist = []
	diff = thresh+1.
	while diff > thresh:
		#
		if Parallelism == 1:
			code_book, NumPointsinClusters, distortsum, distortmax, NumPoints  = Kmeans_map(obs, code_book)
		if Parallelism == 2:
			# Can be Parallel Map Operations
			code_book1, NumPointsinClusters1, distortsum1, distortmax1, NumPoints1  = Kmeans_map(obs1, code_book)
			code_book2, NumPointsinClusters2, distortsum2, distortmax2, NumPoints2  = Kmeans_map(obs2, code_book)
			#
			#	Following are 4 Reduction Operations
			#	Note maps include local reductions
			code_book = np.add( code_book1, code_book2)
			NumPointsinClusters = np.add( NumPointsinClusters1, NumPointsinClusters2)
			distortsum = distortsum1 + distortsum2
			distortmax = np.maximum(distortmax1, distortmax2)
			NumPoints = NumPoints1 +  NumPoints2
		#
		code_book = np.compress(np.greater(NumPointsinClusters, 0), code_book, 0)
		#	remove code_books that didn't have any members
		#
		j = 0
		nc = code_book.shape[0]
		for i in np.arange(nc):
			if NumPointsinClusters[i] > 0:
				code_book[j,:] = code_book[j,:] / NumPointsinClusters[i]
				j = j + 1
		#
		# Calculate mean discrepancy
		distortavg = distortsum/NumPoints
		avg_dist.append(distortavg)
		if len(avg_dist) > 1:
		    diff = avg_dist[-2] - avg_dist[-1]
		    #	Change in average discrepancy
		    #	Can also test on average discrepancy itself
	#
	return code_book, distortavg, distortmax
	# Return Centroid array and final average discrepancy
#
#	Execute Kmeans map functions in parallel
#	No test on cluster count as this must be summed over maps
def Kmeans_map(obs, code_book):
	No = obs.shape[0]
	nc = code_book.shape[0]
	# nc is current number of clusters (may decrease if zero clusters last iteration)
	#
	#compute membership and distances between obs and code_book
	obs_code, distort = vq(obs, code_book)
	distortsum = np.sum(distort)
	distortmax = np.amax(distort)
	#
	# vq returns an indexing array obs_code mapping rows of obs (the points) to code_book (the centroids)
	# distort is an array of length No that has difference between observation and chosen centroid
	# vq stands for vector quantization and is provided in SciPy
	#
	VectorDimension = obs.shape[1]
	NewCode_Book = np.zeros([nc, VectorDimension])
	NumPointsinClusters = np.zeros([nc])
	for i in np.arange(nc):
		#	Loop over clusters labelled with i
		cell_members = np.compress(np.equal(obs_code, i), obs, 0)
		NumPointsinClusters[i] = cell_members.shape[0]
		#	Extract Points in this Cluster; extract points whose quantization label is i
		#
		NewCode_Book[i] = np.sum(cell_members, 0)
		#	Calculate centroid of i'th cluster
	return NewCode_Book, NumPointsinClusters, distortsum, distortmax, No 
		
Radii = np.array([ 0.375, 0.55, 0.6, 0.25 ])

#	Set these values 
#	SciPy default Thresh = 1.0E-5 Parallelism = 1 MaxMean = 1 NumIterations = 20 
Thresh = 1.0E-5
Parallelism = 1
MaxMean = 1
NumIterations = 1

nClusters = 4
nRepeat =   250
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
centroids,error = kmeans_gcf(data,2, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

# some plt.plotting using numpy's logical indexing
plt.figure("Clustering K=2 Large Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=2 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
 data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()

# computing K-Means with K = 4 (4 clusters)
centroids4,error = kmeans_gcf(data,4, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

# some plt.plotting using numpy's logical indexing
plt.figure("Clustering K=4 Large Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=4 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx4==0,0],data[idx4==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx4==1,0],data[idx4==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx4==2,0],data[idx4==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx4==3,0],data[idx4==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(centroids4[:,0],centroids4[:,1],'sg',markersize=8)
plt.show()

# computing K-Means with K = 6 (6 clusters)
centroids,error = kmeans_gcf(data,6, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

# some plt.plotting using numpy's logical indexing
plt.figure("Clustering K=6 Large Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=6 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx==0,0],data[idx==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx==1,0],data[idx==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx==2,0],data[idx==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx==3,0],data[idx==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(data[idx==4,0],data[idx==4,1],marker='o',markerfacecolor='green', ls ='none')
plt.plot(data[idx==5,0],data[idx==5,1],marker='o',markerfacecolor='magenta', ls ='none')
plt.plot(centroids[:,0],centroids[:,1],'sk',markersize=8)
plt.show()

# computing K-Means with K = 8 (8 clusters)
centroids4,error = kmeans_gcf(data,8, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

# some plt.plotting using numpy's logical indexing
plt.figure("Clustering K=8 Large Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=8 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx4==0,0],data[idx4==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx4==1,0],data[idx4==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx4==2,0],data[idx4==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx4==3,0],data[idx4==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(data[idx4==4,0],data[idx4==4,1],marker='o',markerfacecolor='green', ls ='none')
plt.plot(data[idx4==5,0],data[idx4==5,1],marker='o',markerfacecolor='magenta', ls ='none')
plt.plot(data[idx4==6,0],data[idx4==6,1],marker='o',markerfacecolor='yellow', ls ='none')
plt.plot(data[idx4==7,0],data[idx4==7,1],marker='o',markerfacecolor='cyan', ls ='none')
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
centroids,error = kmeans_gcf(data,2, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx,_ = vq(data,centroids)


# some plt.plotting using numpy's logical indexing
plt.figure("Clustering K=2 Small Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=2 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()


# computing K-Means with K = 4 (4 clusters)
centroids4,error = kmeans_gcf(data,4, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

# some plt.plotting using numpy's logical indexing
plt.figure("Clustering K=4 Small Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=4 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
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
centroids,error = kmeans_gcf(data,2, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

#
plt.figure("Clustering K=2 Very Large Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=2 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
plt.show()


# computing K-Means with K = 4 (4 Very Large clusters)
centroids4,error = kmeans_gcf(data,4, NumIterations, Thresh, Parallelism, MaxMean)
# assign each sample to a cluster
idx4,_ = vq(data,centroids4)

#
plt.figure("Clustering K=4 Very Large Radius Kmeans parallel {0} MaxMean {1} Iter {2}".format(Parallelism, MaxMean, NumIterations))
plt.title("K=4 Kmeans parallel {0} MaxMean {1} Iter {2} Distort {3:5.3f}".format(Parallelism, MaxMean, NumIterations, error))
plt.plot(data[idx4==0,0],data[idx4==0,1],marker='o',markerfacecolor='blue', ls ='none')
plt.plot(data[idx4==1,0],data[idx4==1,1],marker='o',markerfacecolor='red', ls ='none')
plt.plot(data[idx4==2,0],data[idx4==2,1],marker='o',markerfacecolor='orange', ls ='none')
plt.plot(data[idx4==3,0],data[idx4==3,1],marker='o',markerfacecolor='purple', ls ='none')
plt.plot(centroids4[:,0],centroids4[:,1],'sg',markersize=8)
plt.show()
