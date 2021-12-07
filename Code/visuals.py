import matplotlib as matplotlib
import numpy as np
import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn; seaborn.set()

df = pd.read_csv('../Data/Disasters_and_economic_impact_by_year.csv')
print(df.head())

#time series of all weather
allDisasters = df.plot(x="Year", y="All natural disasters")
allDisasters.figure.savefig('../Visuals/allDisasters.png')

drought = df.plot(x="Year", y="Drought")
drought.figure.savefig('../Visuals/drought.png')

extremeT = df.plot(x="Year", y="Extreme temperature")
extremeT.figure.savefig('../Visuals/extremeT.png')

extremeW = df.plot(x="Year", y="Extreme weather")
extremeW.figure.savefig('../Visuals/extremeW.png')

flood = df.plot(x="Year", y="Flood")
flood.figure.savefig('../Visuals/flood.png')

landslide = df.plot(x="Year", y="Landslide")
landslide.figure.savefig('../Visuals/landslide.png')

wildfire = df.plot(x="Year", y="Wildfire")
wildfire.figure.savefig('../Visuals/wildfire.png')


#time series of costs of weather
allDisastersCost = df.plot(x="Year", y="TotalCost: All natural disasters")
allDisastersCost.figure.savefig('../Visuals/allDisastersCost.png')

droughtCost = df.plot(x="Year", y="TotalCost: Drought")
droughtCost.figure.savefig('../Visuals/droughtCost.png')

extremeTCost = df.plot(x="Year", y="TotalCost: Extreme temperature")
extremeTCost.figure.savefig('../Visuals/extremeTCost.png')

extremeWCost = df.plot(x="Year", y="TotalCost: Extreme weather")
extremeWCost.figure.savefig('../Visuals/extremeWCost.png')

floodCost = df.plot(x="Year", y="TotalCost: Flood")
floodCost.figure.savefig('../Visuals/floodCost.png')

landslideCost = df.plot(x="Year", y="TotalCost: Landslide")
landslideCost.figure.savefig('../Visuals/landslideCost.png')

wildfireCost = df.plot(x="Year", y="TotalCost: Wildfire")
wildfireCost.figure.savefig('../Visuals/wildfireCost.png')



