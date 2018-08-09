''' This file contains the code for the unit "The Elusive Mr. Higgs". It explains the experiment with higgs signal and background signal under different settings'''

import numpy as np
import matplotlib.pyplot as plt
import pylab

plt.show()
''' Create the background for the setup and plot the same'''
testrand = np.random.rand(42000)                    #A random array have 42000 elements according to the uniform distribution. The numbers generated will between 0 and 1
Base = 110 + 30* np.random.rand(42000)              #Generating a uniform background(base) between a 110 GeV and 140 GeV 
index = (1.0 - 0.5* (Base-110)/30) > testrand       #To create a boolean index which has True for 100% samples at 110GeV; This percentage reduces linearly as the value for background increases and has ture for 50% samples as 140 GeV
sloping = Base[index]                               #This generates a sloping background. Here the values in base corresponding the True values in "index" are retained rest are discarded. So this has a distribution as desribed above
####Plotting - Sloping Background. 
####See The Plot named "Sloping"
plt.figure("Sloping")
plt.hist(sloping, bins=15, range =(110,140))
plt.title("Sloping Background from 42000 events", backgroundcolor = "white")

'''Create a Gaussian Higgs signal(Gaussian signal is what we will get due to error in measurement). The width of the Gaussian indicated the extent of measurement error. This signal has 300 samples. '''
gauss = 2 * np.random.randn(300) +126               #The signal is centered at 126 GeV and has a width of 2.
narrowGauss = 0.5 * np.random.randn(300) +12        #A signal with centered at 126 GeV and width of 0.5(Error in measurement is less than previous signal"
####Plotting - The Higgs Signal with width 2.0. 
####See The Plot named "HiggsAlone"
plt.figure("HiggsAlone")
plt.hist(gauss, bins=15, range =(110,140))
plt.title("2Gev Higgs in 2 GeV bins on its own", backgroundcolor = "white")


'''Create the actual Signal by combining the higs signals(Gaussian signals) and the background signals.'''
total = np.concatenate((sloping, gauss))            #Accumalate the sloping Background and gauss(width = 2.0)
narrowTotal = np.concatenate((sloping, narrowGauss)) #Accumalate the sloping background and narrowGauss(width = 0.5)
####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 0.5. The plot has 15 bins(each bin represents 2 GeV). 
####See The Plot named "Total Narrow Higgs"
plt.figure("Total Narrow Higgs")
plt.hist(narrowTotal, bins=15, range =(110,140), alpha = 0.5)   #Total Signal
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5)       #Sloping Signal.
plt.hist(narrowGauss, bins=15, range =(110,140), alpha = 0.5)   #Only the Higgs Signal.
plt.title("0.5 Gev Higgs in 2 GeV bins with Sloping Background", backgroundcolor = "white")

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 0.5. The plot has 30 bins(each bin represents 1GeV).
####See The Plot named "Total Narrow Higgs Bin 1 GeV"
plt.figure("Total Narrow Higgs Bin 1 GeV")
plt.hist(narrowTotal, bins=30, range =(110,140), alpha = 0.5)   #Total Signal
plt.hist(sloping, bins=30, range =(110,140), alpha = 0.5)       #Sloping Signal.      
plt.hist(narrowGauss, bins=30, range =(110,140), alpha = 0.5)   #Only the Higgs Signal.
plt.title("0.5 Gev Higgs in 1 GeV bins with Sloping Background", backgroundcolor = "white")

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 0.5. The plot has 60 bins(each bin represents 0.5GeV).
####See The Plot named "Total Narrow Higgs Bin 0.5 GeV"
plt.figure("Total Narrow Higgs Bin 0.5 GeV")
plt.hist(narrowTotal, bins=60, range =(110,140), alpha = 0.5)   #Total Signal
plt.hist(sloping, bins=60, range =(110,140), alpha = 0.5)       #Sloping Signal.
plt.hist(narrowGauss, bins=60, range =(110,140), alpha = 0.5)   #Only the Higgs Signal.
plt.title("0.5 Gev Higgs in 0.5 GeV bins with Sloping Background", backgroundcolor = "white")

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) signal where Higgs Signal has width 2.0. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Wide Higgs Bin 2 GeV"
plt.figure("Total Wide Higgs Bin 2 GeV")
values, binedges, junk = plt.hist(total, bins=15, range =(110,140), alpha = 0.5, color = "blue")     #Total Signal. We also store the histogram values(number of members per bin) and binedges.
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5, color = "green")                           #Sloping Signal.
plt.hist(gauss, bins=15, range =(110,140), alpha = 0.5, color = "red")                               #Only the Higgs Signal.
plt.title("2 Gev Higgs in 2 GeV bins with Sloping Background", backgroundcolor = "white")

'''Computing the bin Centers and Errors.'''
centers = 0.5*(binedges[1:] + binedges[:-1])                            #Computing bin center as the average of its 2 bin-edges.
errors = np.sqrt(values)                                                #Computing expected error as the square root of values.
####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) and expected errors where Higgs Signal has width 2.0. The plot has 60 bins(each bin represents 0.5GeV).
####See The Plot named "Total Wide Higgs Bin 2 GeV with errors" 
plt.figure("Total Wide Higgs Bin 2 GeV with errors")
plt.hist(total, bins=15, range =(110,140), alpha = 0.5, color = "blue")                                 #The total signal
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5, color = "green")                              #Sloping Signal.
plt.hist(gauss, bins=15, range =(110,140), alpha = 0.5, color = "red")                                  #Only the Higgs Signal.
plt.errorbar(centers, values, yerr = errors, ls='None', marker ='x', color = 'black', markersize= 6.0 ) #The error bar
plt.title("2 Gev Higgs in 2 GeV bins with Sloping Background + Errors", backgroundcolor = "white")


'''Creating a Higgs Signal with 30000 elements. If we use this against the original backgrounds, we study the effect of making the Higgs 100 times more likely(The original number of Higgs samples was 300).'''
gaussbig = 2 * np.random.randn(30000) +126                  #Creating a Higgs Signal with 30000 elements and width of 2.0
gaussnarrowbig = 0.5 * np.random.randn(30000) +126          #Creating a Higgs Signal with 30000 elements and width of 0.5(less error in measurement than previous case)
totalbig = np.concatenate((sloping, gaussbig))
####Plotting - The Pure Higgs Signals with weight 0.5 and 2. The signal with 30,000 elements is used. Plot has 60 bins(each of size .5GeV).
####See The Plot named "30000 Higgs in 0.5 GeV bins" 
plt.figure("30000 Higgs in 0.5 GeV bins")
plt.hist(gaussnarrowbig, bins=60, range =(110,140), alpha = 0.5) #Higgs signal 
plt.hist(gaussbig, bins=60, range =(110,140), alpha = 0.5)
plt.title("30000 Narrow and Wide Higgs in 0.5 GeV bins", backgroundcolor = "white")

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 2.0 and is 100 times more frequent. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Wide Higgs Bin 2 GeV 100 times Higgs" 
plt.figure("Total Wide Higgs Bin 2 GeV 100 times Higgs")
plt.hist(totalbig, bins=15, range =(110,140), alpha = 0.5)                          #Total signal with Higgs being 100 times more frequent
plt.hist(sloping, bins=15, range =(110,140), alpha = 0.5)                           #sloping background
plt.hist(gaussbig, bins=15, range =(110,140), alpha = 0.5)                          #Higgs signal with 30,000 elements
plt.title("Total Wide Higgs Bin 2 GeV 100 times Higgs", backgroundcolor = "white")

'''Creating a setup with 1% data. Now the background has initially 420 elements'''
testrand420 = np.random.rand(420)                               #Creating random array with 420 elements.                               
Base420 = 110 + 30* np.random.rand(420)                         #Creating Background with 420 events 
index420 = (1.0 - 0.5* (Base420-110)/30) > testrand420          #Creating index to get the sloping background.
Sloping420 = Base420[index420]                                  #Creating Sloping Background
#### Plot - Plotting the 1% background data. Plot has 15 bins(each 2GeV)
####See The Plot named "Sloping 420 Events" 
plt.figure("Sloping 420 Events")
plt.hist(Sloping420, bins=15, range =(110,140))
plt.title("Sloping Background from 420 events (1%)", backgroundcolor = "white")


'''Creating setup with 10% data(4200 elements for background, 30 elements for Higgs signal) and computing the errors.'''
testrand4200 = np.random.rand(4200)                             #Creating random array with 4200 elements.  
Base4200 = 110 + 30* np.random.rand(4200)                       #Creating Background with 4200 events 
index4200 = (1.0 - 0.5* (Base4200-110)/30) > testrand4200       #Creating index to get the sloping background.
Sloping4200 = Base4200[index4200]                               #Creating Sloping Background
gauss30 = 2 * np.random.randn(30) +126                          #Creating Higgs signal with width 2.0 and center at 126GeV
total10percent = np.concatenate((Sloping4200, gauss30))         #Combining the Higgs signal and sloping background
####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) where Higgs Signal has width 2.0 for 10% of data. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Sloping Background 10% Data" 
plt.figure("Total Sloping Background 10% Data")
values10percent, binedges10percent, junk = plt.hist(total10percent, bins=15, range =(110,140), alpha = 0.5, color = "blue") #Total signal and storing the number values/bin and the bin edges.
plt.hist(Sloping4200, bins=15, range =(110,140), alpha = 0.5, color = "green")                                              #Sloping background
plt.hist(gauss30, bins=15, range =(110,140), alpha = 0.5, color = "red")                                                    #Higgs Signal(width 2.0)
plt.title("Total with Sloping Background from 4200 events (10%)", backgroundcolor = "white")

####Plotting - The 3 kinds of signals(Sloping Background, Higgs Signal, Combined Signal) and the error where Higgs Signal has width 2.0 for 10% of data. The plot has 15 bins(each bin represents 2GeV).
####See The Plot named "Total Sloping Background 10% Data with errors"
plt.figure("Total Sloping Background 10% Data with errors")
centers10percent = 0.5*(binedges10percent[1:] + binedges10percent[:-1])             #Computing the bin centers
errors10percent = np.sqrt(values10percent)                                          #Computing expected errors
plt.hist(total10percent, bins=15, range =(110,140), alpha = 0.5, color = "blue")    #Plotting the total signal
plt.hist(Sloping4200, bins=15, range =(110,140), alpha = 0.5, color = "green")      #Plotting the sloping background
plt.hist(gauss30, bins=15, range =(110,140), alpha = 0.5, color = "red")            #Plotting the Higgs Signal
plt.errorbar(centers10percent, values10percent, yerr = errors10percent, ls='None', marker ='x', color = 'black', markersize= 6.0 ) #Plotting the error
plt.title("Total with Sloping Background from 4200 events (10%) + Errors", backgroundcolor = "white")
pylab.show()
