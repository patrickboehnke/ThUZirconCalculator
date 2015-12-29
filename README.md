# ThUZirconCalculator
A Python program that corrects U-series zircon age measurements for the initial Th in the melt

This program uses a resampling approach to calculate uncertainties in the age due to the correction for the initial 230Th.

To use this program please download all of the files extract them into a directory.

Then use your favorite Python interpreter to run this program.

If you do not have Python installed please check out the following links to install Python:
https://wiki.python.org/moin/PythonDistributions

I personally use Enthought Canopy which has a free license and a great academic license: https://www.enthought.com/products/canopy/

Please put your own data in the Example.csv file in the following format:

Column 1: 238U/232Th activity ratio
Column 2: 1 sigma uncertainty on 238U/232Th activity ratio
Column 3: 230Th/232Th activity ratio
Column 4: 1 sigma uncertainty on 230Th/232Th activity ratio

If you have problems, questions, or suggestions please contact me at: pboehnke _@_ gmail _._ com (remove _ and spaces)




References:
1) Boehnke, P., Barboni, M., & Bell, E. A. (2015). Zircon U/Th Model Ages in the Presence of Melt Heterogeneity. Quaternary Geochronology, Submitted.
