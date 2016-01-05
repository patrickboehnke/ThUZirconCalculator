# ThUZirconCalculator
A Python program that corrects U-series zircon age measurements for the initial Th in the melt

This program uses a resampling approach to calculate uncertainties in the age due to the correction for the initial 230Th.

To use this program please download all of the files extract them into a directory.

Then use your favorite Python interpreter to run this program.

If you do not have Python installed please check out the following links to install Python:
https://wiki.python.org/moin/PythonDistributions

I personally use Enthought Canopy which has a free license and a great academic license: https://www.enthought.com/products/canopy/

Please put your own data in the Example.csv file in the following format:

The original example data is from the Belfond Dome data provided in reference 2

Column 1: 238U/232Th activity ratio
Column 2: 1 sigma uncertainty on 238U/232Th activity ratio
Column 3: 230Th/232Th activity ratio
Column 4: 1 sigma uncertainty on 230Th/232Th activity ratio

Output will be provided in a file called output_example.csv

Output values are arranged as m value and one sigma uncertainties (column 1 and 2 respectively).
m values are explained in reference 3

If you have problems, questions, or suggestions please contact me at: pboehnke _@_ gmail _._ com (remove _ and spaces)




References:
1) Boehnke, P., Barboni, M., & Bell, E. A. (2016). Zircon U/Th Model Ages in the Presence of Melt Heterogeneity. Quaternary Geochronology, Submitted.

2) Schmitt, A. K., Stockli, D. F., Lindsay, J. M., Robertson, R., Lovera, O. M., & Kislitsyn, R. (2010). Episodic growth and homogenization of plutonic roots in arc volcanoes from combined U-Th and (U-Th)/He zircon dating. Earth and Planetary Science Letters, 295, 91–103. doi:10.1016/j.epsl.2010.03.028

3) Schmitt, A. K. (2011). Uranium Series Accessory Crystal Dating of Magmatic Processes. Annual Review of Earth and Planetary Sciences, 39(1), 321–349. doi:10.1146/annurev-earth-040610-133330
