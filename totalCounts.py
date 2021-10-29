#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Natural Disasters Counts
"""
import pandas as pd

disastersDF = pd.read_csv('natural_disasters_cleaned.csv')

totalDisasters = disastersDF['All natural disasters'].sum()
print(totalDisasters)

totalDrought = disastersDF['Drought'].sum()
print(totalDrought)

totalExtremeTemperature = disastersDF['Extreme temperature'].sum()
print(totalExtremeTemperature)

totalExtremeWeather = disastersDF['Extreme weather'].sum()
print(totalExtremeWeather)

totalFlood = disastersDF['Flood'].sum()
print(totalFlood)

totalLandslide = disastersDF['Landslide'].sum()
print(totalLandslide)

totalWildfire = disastersDF['Wildfire'].sum()
print(totalWildfire)

economicDF = pd.read_csv('natural_disaster_economic_impact_cleaned.csv')

totalEconomic = economicDF['TotalCosts'].sum()
print(totalEconomic)