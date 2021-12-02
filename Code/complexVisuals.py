import matplotlib as matplotlib
import numpy as np
import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../Disasters_and_economic_impact_by_year.csv')
#print(df.head())

allDisastersandCost = sns.scatterplot(data=df, x="Year",y="All natural disasters", size="TotalCost: All natural disasters", legend=False, sizes=(20, 2000))
allDisastersandCost.figure.savefig('allDisastersandCost.pdf')

droughtandCost = sns.scatterplot(data=df, x="Year",y="Drought", size="TotalCost: Drought", legend=False, sizes=(20, 2000))
droughtandCost.figure.savefig('droughtandCost.pdf')

extremeTandCost = sns.scatterplot(data=df, x="Year",y="Extreme temperature", size="TotalCost: Extreme temperature", legend=False, sizes=(20, 2000))
extremeTandCost.figure.savefig('extremeTandCost.pdf')

extremeWandCost = sns.scatterplot(data=df, x="Year",y="Extreme weather", size="TotalCost: Extreme weather", legend=False, sizes=(20, 2000))
extremeWandCost.figure.savefig('extremeWandCost.pdf')

floodandCost = sns.scatterplot(data=df, x="Year",y="Flood", size="TotalCost: Flood", legend=False, sizes=(20, 2000))
floodandCost.figure.savefig('floodandCost.pdf')

landslideandCost = sns.scatterplot(data=df, x="Year",y="Landslide", size="TotalCost: Landslide", legend=False, sizes=(20, 2000))
landslideandCost.figure.savefig('landslideandCost.pdf')

wildFireandCost = sns.scatterplot(data=df, x="Year",y="Wildfire", size="TotalCost: Wildfire", legend=False, sizes=(20, 2000))
wildFireandCost.figure.savefig('wildFireandCost.pdf')
