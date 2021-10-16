#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Cleaning for Natural Disasters Dataset
Haley Egan
10/15/21
"""
#data cleaning of dataset for semester projects - Natural Disasters
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
Dataset: Number of natural disasters dataset 
- remove missing values
- remove earthquakes - not climate related 
- remove volcanic activity - not climate related
- remove mass movement (dry) - not climate related (I think)
- remove “impact” - unknown relevancy and only one in dataset 
- remove ‘code’ column 
- rename Entity as Disaster 
- rename 'Number of reported natural disasters (reported disasters)' as 'Number_of_Disasters'
'''

import pandas as pd

#open csv file     
df = pd.read_csv('natural_disaster_events.csv') #open csv as dataframe 
df.head()
#print(df)
    
first_row = df.iloc[0]  #get first row  
#print(first_row)    

#rename columns
df = df.rename(columns={'Entity': 'Disaster', 'Number of reported natural disasters (reported disasters)': 'Number_of_Disasters'})

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


#write changes to csv file
df.to_csv('natural_disasters_cleaned.csv', index=False)


