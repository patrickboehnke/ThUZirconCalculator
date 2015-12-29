# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:51:54 2015

@author: Patrick Boehnke

If you use this code please cite:

Boehnke, P., Barboni, M., & Bell, E. A. (2015). Zircon U/Th Model Ages in the Presence of Melt Heterogeneity. Quaternary Geochronology, Submitted.

For comments please contact: pboehnke @ gmail . com (remove spaces)
"""

import numpy as np
import copy

#This loads the data file please change it to the right file name
#Data file must be in same directory as this python script
Data = np.loadtxt("Example.csv", delimiter=",")
U238Th232 = Data[:, 0]
U238Th2321sig = Data[:, 1]
Th230Th232 = Data[:, 2]
Th230Th2321sig = Data[:, 3]

ModelSlope = copy.deepcopy(U238Th232)
ModelSlopeUnc = copy.deepcopy(U238Th232)
EquiPoint = np.zeros(len(U238Th232))

#Partition Coefficients for U relative to Th
#Value calculated and justified in manuscript
#If you wish to use your own value make the change here 
DUDTh = 7
DUDThunc = 0.4 #Uncertainty at 1 sigma

for iter1 in range(len(U238Th232)):
    NewSlope = np.zeros(1000)
    for iter2 in range(0,1000):
        Slope = 1.1
        while(Slope > 1):
            U238Th232Samp = np.random.randn()*U238Th2321sig[iter1] + U238Th232[iter1]
            Th230Th232Samp = np.random.randn()*Th230Th2321sig[iter1] + Th230Th232[iter1]
            PartCoef = np.random.randn()*DUDThunc + DUDTh
            U238Th232M = U238Th232Samp/PartCoef
            Th230Th232M = np.random.randn()*0.16*U238Th232M + U238Th232M
            
            Slope = (Th230Th232Samp - Th230Th232M)/(U238Th232Samp - U238Th232M)
        NewSlope[iter2] = Slope
    ModelSlope[iter1] = np.mean(NewSlope)
    ModelSlopeUnc[iter1] = np.std(NewSlope)


writeoutarray = np.zeros((len(ModelSlope), 2))
for iter1 in range(0, len(ModelSlope)):
    writeoutarray[iter1, 0] = ModelSlope[iter1]
    writeoutarray[iter1, 1] = ModelSlopeUnc[iter1]
np.savetxt("output_example.csv", writeoutarray, delimiter=",")
