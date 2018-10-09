import numpy as np
import matplotlib.pyplot as plt
import pylab

Base = 110 + 30* np.random.rand(42000)
# Base is set of observations with an expected 2800 background events  per bin
# Note we assume here flat but in class I used a "sloping" curve that represented experiment better
gauss = 2 * np.random.randn(300) + 126
# Gauss is Number of Higgs particles
simpletotal = np.concatenate((Base, gauss))
# simpletotal is Higgs+Background
plt.figure("Total Wide Higgs Bin 2 GeV")
values, binedges, junk = plt.hist(simpletotal, bins=15, range =(110,140), alpha = 0.5, color="green")
centers = 0.5*(binedges[1:] + binedges[:-1])
# centers is center of each bin
# values is number of events in each bin
# :-1 is same as :Largest Index-1
# binedges[:-1] gets you lower limit of bin
# 1: gives you array starts at second index (labelled 1 as first index 0)
# binedges[1:] is upper limit of each bin
# Note binedges has Number of Bins + 1 entries; centers has Number of Bins entries
errors =np.sqrt(values)
# errors is expected error for each bin
plt.hist(Base, bins=15, range =(110,140), alpha = 0.5, color="blue")
plt.hist(gauss, bins=15, range =(110,140), alpha = 0.5, color="red")
plt.errorbar(centers, values, yerr = errors, ls='None', marker ='x', color = 'black', markersize= 6.0 )
plt.title("Uniform Background from 42000 events; 2 Gev Higgs", backgroundcolor = "white")
# For Agg backend
pylab.show()
plt.show()
