#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Natural Disasters Counts
"""
import pandas as pd

disastersDF = pd.read_csv('../Data/natural_disasters_cleaned.csv')

totalDisasters = disastersDF['All natural disasters'].sum()
print("Total Disasters:", int(totalDisasters))

totalDrought = disastersDF['Drought'].sum()
print("Total number of Droughts:", int(totalDrought))

totalExtremeTemperature = disastersDF['Extreme temperature'].sum()
print("Total number of Extreme Temperature Events:", int(totalExtremeTemperature))

totalExtremeWeather = disastersDF['Extreme weather'].sum()
print("Total number of Extreme Weather Events:", int(totalExtremeWeather))

totalFlood = disastersDF['Flood'].sum()
print("Total number of Floods:", int(totalFlood))

totalLandslide = disastersDF['Landslide'].sum()
print("Total number of Landslides:", int(totalLandslide))

totalWildfire = disastersDF['Wildfire'].sum()
print("Total number of Wildfires:", int(totalWildfire))

economicDF = pd.read_csv('../Data/natural_disaster_economic_impact_cleaned.csv')

totalEconomic = economicDF['TotalCosts'].sum()
print("Total economic impact:", totalEconomic)
