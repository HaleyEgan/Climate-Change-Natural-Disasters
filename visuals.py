import matplotlib as matplotlib
import numpy as np
import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn; seaborn.set()

df = pd.read_csv('../Disasters_and_economic_impact_by_year.csv')
print(df.head())

#time series of all weather
allDisasters = df.plot(x="Year", y="All natural disasters")
allDisasters.figure.savefig('allDisasters.pdf')

drought = df.plot(x="Year", y="Drought")
drought.figure.savefig('drought.pdf')

extremeT = df.plot(x="Year", y="Extreme temperature")
extremeT.figure.savefig('extremeT.pdf')

extremeW = df.plot(x="Year", y="Extreme weather")
extremeW.figure.savefig('extremeW.pdf')

flood = df.plot(x="Year", y="Flood")
flood.figure.savefig('flood.pdf')

landslide = df.plot(x="Year", y="Landslide")
landslide.figure.savefig('landslide.pdf')

wildfire = df.plot(x="Year", y="Wildfire")
wildfire.figure.savefig('wildfire.pdf')


#time series of costs of weather
allDisastersCost = df.plot(x="Year", y="TotalCost: All natural disasters")
allDisastersCost.figure.savefig('allDisastersCost.pdf')

droughtCost = df.plot(x="Year", y="TotalCost: Drought")
droughtCost.figure.savefig('droughtCost.pdf')

extremeTCost = df.plot(x="Year", y="TotalCost: Extreme temperature")
extremeTCost.figure.savefig('extremeTCost.pdf')

extremeWCost = df.plot(x="Year", y="TotalCost: Extreme weather")
extremeWCost.figure.savefig('extremeWCost.pdf')

floodCost = df.plot(x="Year", y="TotalCost: Flood")
floodCost.figure.savefig('floodCost.pdf')

landslideCost = df.plot(x="Year", y="TotalCost: Landslide")
landslideCost.figure.savefig('landslideCost.pdf')

wildfireCost = df.plot(x="Year", y="TotalCost: Wildfire")
wildfireCost.figure.savefig('wildfireCost.pdf')



