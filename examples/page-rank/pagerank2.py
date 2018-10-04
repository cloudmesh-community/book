'''this file has code to compute the page rank as per the adjacency matrix'''

# http://glowingpython.blogspot.com/2011/05/four-ways-to-compute-google-pagerank.html
from numpy import *

def powerMethodBase(A,x0,iter):
 """ basic power method. Stops after the number of iteration as specified in the "iter" paramneter."""
 for i in range(iter):
  x0 = dot(A,x0)
  x0 = x0/linalg.norm(x0,1)
 return x0

def powerMethodBase1(A,x0,thresh,iter):
  """ basic power method. Stops after the number of iteration as specified in the "iter" paramneter or after the improvement is less than threshold(thresh parameter) """
  x0 = x0/linalg.norm(x0,1)
  x1 = x0
  for i in range(iter):
   x0 = dot(A,x0)
   x0 = x0/linalg.norm(x0,1)
   stop = linalg.norm(x0-x1,1)
   if stop < thresh:
    print "Method 5 Stop ",stop, " After ", i, " iterations compare to default", iter 
    break
   x1 = x0
  return x0
 
def powerMethod(A,x0,m,iter):
 """ power method modified to compute
     the maximal real eigenvector 
     of the matrix M built on top of the input matrix A """
 n = A.shape[1]
 delta = m*(array([1]*n,dtype='float64')/n) # array([1]*n is [1 1 ... 1] n times
 for i in range(iter):
  x0 = dot((1-m),dot(A,x0)) + delta
 return x0

def maximalEigenvector(A):
 """ using the eig function to compute eigenvectors """
 n = A.shape[1]
 w,v = linalg.eig(A)
 return abs(real(v[:n,0])/linalg.norm(v[:n,0],1))

def linearEquations(A,m):
 """ solving linear equations 
     of the system (I-(1-m)*A)*x = m*s """
 n = A.shape[1]
 C = eye(n,n)-dot((1-m),A)
 b = m*(array([1]*n,dtype='float64')/n)
 return linalg.solve(C,b)

def getTeleMatrix(A,m):
 """ return the matrix M
     of the web described by A """
 n = A.shape[1]
 S = ones((n,n))/n
 return (1-m)*A+m*S

A = array([ [0,     0,     0,     1, 0, 1],
            [1/2.0, 0,     0,     0, 0, 0],
            [0,     1/2.0, 0,     0, 0, 0],
            [0,     1/2.0, 1/3.0, 0, 0, 0],
            [0,     0,     1/3.0, 0, 0, 0],
            [1/2.0, 0,     1/3.0, 0, 1, 0 ] ])

n = A.shape[1] # A is n x n
m = 0.15        #Damping factor of 0.15(indicates the probabilty of the user not chosing any of the links on the page he is on.)
M = getTeleMatrix(A,m)

x0 = ones(n)/ n
x1 = powerMethod(A,x0,m,130)
x2 = powerMethodBase(M,x0,130)
x5 = powerMethodBase1(M,x0,1.0e-6, 130)
x3 = maximalEigenvector(M)
if m > 0.001:
	x4 = linearEquations(A,m)

# comparison of the five methods
print "\nDamping factor ", m, " Matrix Size ", n
print "1 ", x1
print "2 ", x2
print "3 ", x3
if m > 0.001:
	print "4 ", x4
print "5 ", x5

obs = array([ 
	[0,     0, 0, 0, 0, 0, 1/3.0, 0],
	[1/2.0, 0, 1/2.0, 1/3.0, 0, 0, 0, 0],
	[1/2.0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 1/2.0, 1/3.0, 0, 0, 1/3.0, 0],
	[0, 0, 0, 1/3.0, 1/3.0, 0, 0, 1/2.0],
	[0, 0, 0, 0, 1/3.0, 0, 0, 1/2.0],		
	[0, 0, 0, 0, 1/3.0, 1, 1/3.0, 0] ])
            
n = obs.shape[1] # obs is n x n
m = 0.0	# No damping
M = getTeleMatrix(obs,m)

x0 = ones(n)/ n
x1 = powerMethod(obs,x0,m,130)
x2 = powerMethodBase(M,x0,130)
x5 = powerMethodBase1(M,x0,1.0e-7, 130)
x3 = maximalEigenvector(M)
if m > 0.001:
	x4 = linearEquations(H,m)

# comparison of the five methods
print "\nDamping factor ", m, " Matrix Size ", n
print "1 ", x1
print "2 ", x2
print "3 ", x3
if m > 0.001:
	print "4 ", x4
print "5 ", x5
