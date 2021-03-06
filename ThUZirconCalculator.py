# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:51:54 2015

@author: Patrick Boehnke

If you use this code please cite:

Boehnke, P., Barboni, M., & Bell, E. A. (2016). Zircon U/Th Model Ages in the Presence of Melt Heterogeneity. Quaternary Geochronology, Submitted.

For comments please contact: pboehnke @ gmail . com (remove spaces)
"""

import numpy as np

#Partition Coefficients for U relative to Th
#Value calculated and justified in manuscript
#If you wish to use your own value make the change here 
DUDTh = 7
DUDThunc = 0.4 #Uncertainty at 1 sigma

#If you want to use a normal distribution put 1 if you want to resample the database put 0
#We recommend using 1 as it provides a more conservative estimate of the uncertainties
EquiUncertaintyModel = 1

#Spread of compiled volcanic data from the equiline at 1 sigma
EquilineUncertainty = 0.15 #Reported at 1 sigma

if EquiUncertaintyModel == 0:
    EquilineSpread = np.loadtxt("Spread.csv", delimiter=",")

#This sets the number of samples for each sample calculation
#Higher is better but takes longer, 1000 is the default
NumIterations = 1000

#This loads the data file please change it to the right file name
#Data file must be in same directory as this python script
Data = np.loadtxt("Example.csv", delimiter=",")

U238Th232 = Data[:, 0]
U238Th2321sig = Data[:, 1]
Th230Th232 = Data[:, 2]
Th230Th2321sig = Data[:, 3]

ModelSlope = np.copy(U238Th232)
ModelSlopeUnc = np.copy(U238Th232)
NewSlope = np.zeros(NumIterations)


for iter1 in range(len(U238Th232)):    
    for iter2 in range(NumIterations):
        U238Th232Samp = np.random.randn()*U238Th2321sig[iter1] + U238Th232[iter1]
        Th230Th232Samp = np.random.randn()*Th230Th2321sig[iter1] + Th230Th232[iter1]
        PartCoef = np.random.randn()*DUDThunc + DUDTh
        U238Th232M = U238Th232Samp/PartCoef
        if EquiUncertaintyModel == 1:
            Th230Th232M = np.random.randn()*EquilineUncertainty*U238Th232M + U238Th232M
        else:
            Th230Th232M = U238Th232M + np.random.choice(EquilineSpread)
        
        Slope = (Th230Th232Samp - Th230Th232M)/(U238Th232Samp - U238Th232M)
        if Slope > 1:
            NewSlope[iter2] = 1
        elif Slope < 0:
            NewSlope[iter2] = 0
        else:
            NewSlope[iter2] = Slope
    ModelSlope[iter1] = np.mean(NewSlope)
    ModelSlopeUnc[iter1] = np.std(NewSlope)


writeoutarray = np.zeros((len(ModelSlope), 2))
for iter1 in range(0, len(ModelSlope)):
    writeoutarray[iter1, 0] = ModelSlope[iter1]
    writeoutarray[iter1, 1] = ModelSlopeUnc[iter1]
np.savetxt("output_example.csv", writeoutarray, delimiter=",")
