#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Cleaning for Natural Disasters Economic Impact Dataset
Haley Egan
10/15/21
"""
'''
Content
This dataset contains information on global occurrences of natural disasters and the economic damage 
caused by them. The included types of natural disaster are 'Drought', 'Earthquake', 'Extreme temperature', 
'Extreme weather', 'Flood', 'Impact', 'Landslide', 'Mass movement (dry)', 'Volcanic activity' and 'Wildfire'. 
It also includes information on all these natural disasters combined. 
The time period is 1900-2018 with several missing values.

Two Datasets: number of natural disasters, and economic damage from natural disasters

This dataset is a subset of the data available on https://ourworldindata.org/natural-disasters

Reference:
https://ourworldindata.org/natural-disasters (data published by EMDAT (2019): 
OFDA/CRED International Disaster Database, Université catholique de Louvain – Brussels – Belgium)

DATA CLEANING
Dataset: Economic damage from natural disasters
- remove missing values 
- remove ‘code’ column 
- remove years where "Total economic damage from natural disasters (US$)" = 0 (will skew data)
- remove earthquakes - not climate related 
- remove volcanoes - not climate related
- remove mass movement (dry) - not climate related 
- remove “impact” - unknown relevancy and only one in dataset 
- rename last column 
'''

import pandas as pd
import numpy as np
from numpy import nan as NA


#open csv file     
df = pd.read_csv('natural_disaster_economic_impact.csv') #open csv as dataframe 
df.head()
#print(df)
    
first_row = df.iloc[0]  #get first row  
#print(first_row)    

#check columns
df.columns

#rename columns
df = df.rename(columns={'Entity': 'Disaster', 'Total economic damage from natural disasters (US$)':'TotalCosts'})

#check columns
df.columns

#remove 'Code' column
df = df.drop(columns=['Code']) #remove 'code' column 
#print(first_row)

#remove 'Earthquake' rows - drop by condition
df = df[df.Disaster != 'Earthquake']
#print(df)

#remove 'Volcanic avtivity' rows
df = df[df.Disaster != 'Volcanic activity']

#remove 'Mass Movement (dry)' rows
df = df[df.Disaster != 'Mass movement (dry)']

#remove 'Impact' rows
df = df[df.Disaster != 'Impact']

#remove rows where TotalCosts = 0 (will skew data, since 0 is actually NAN)
df = df[df.TotalCosts != 0]

#write changes to csv file
df.to_csv('natural_disaster_economic_impact_cleaned.csv', index=False)


