#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Cleaning Object for Natural Disasters Dataset
Haley Egan, Will Johnson
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

Versioning:
- V1: Haley Egan - Initial Commit and Selecting Columns. (10/15/2021)
- V2: Will Johnson - Data Pivoting and OOP structure (10/24/2021)
'''

import pandas as pd

class DisasterData(object):
    '''
    Object class for gathering and cleaning dataset for this project's analsis.

    Attributes:
        - df (DataFrame): a pandas dataframe of the cleaned & pivoted dataset.
        - original_df(DataFrame): a pd dataframe of the original dataset.
        - column_map: Names we give to our columns to make it more readable.
        - final_columns: a list of columns we choose to keep in our dataset.

    Methods:
        - __init__(): instanciates the object.
        - clean_df(): cleans and pivots our dataset.

    Helper Functios:
        - _clean_dataset()
    '''
    def __init__(self, csv_strs = ['natural_disasters_original.csv','natural_disaster_economic_impact_original.csv']):
        '''
        Opens the original file of the dataset and cleans/pivots it.

        Args:
            - csv_str(iter): the paths to the csv files we want as our initial pull.
                - Default: (natural_disasters_original.csv,'natural_disaster_economic_impact.csv')
        '''
        # pull the original datasets
        self.disaster_df = pd.read_csv(csv_strs[0])
        self.economic_df = pd.read_csv(csv_strs[1])

        # The following will act as default values for cleanDf()
        # set our column_map and rename them.
        self.column_map = {
                'Entity': 'Disaster',
                'Number of reported natural disasters (reported disasters)': 'Number_of_Disasters',
                'Total economic damage from natural disasters (US$)':'TotalCosts'
                }


        # a list to select the columns we need, and ignore the ones we don't
        self.final_columns = ['All natural disasters',
                            'Drought',
                            'Extreme temperature',
                            'Extreme weather',
                            'Flood',
                            'Landslide',
                            'Wildfire']

        # add additional columns for the total cost of each method.
        self.final_columns = self.final_columns + ['TotalCost: '+col for col in self.final_columns]

        # Create an empty dataframe for df since we haven't cleand it yet
        self.df = pd.DataFrame()

    def cleanDf(self,cols = None, column_map = None): 
        '''
        takes the self.df object and populates it with a cleaned dataset from our
        original dataset.
        '''
        # unless other arguments are provided, set our column variables based on defaults.
        if not cols:
            cols = self.final_columns
        if not column_map:
            column_map = self.column_map

        # Create 'df' attribute and rename the columns appropriately.
        self.df1 = self.disaster_df.rename(columns=column_map)

        # Re-organize our dataset so that each disaster-type is one column
        self.df1 = self.df1.pivot(columns='Disaster',
                                index='Year',
                                values='Number_of_Disasters')

        # now do the same for df2, our economic dataset
        self.df2 = self.economic_df.rename(columns=column_map)
        self.df2 = self.df2.pivot(columns='Disaster',
                                index='Year',
                                values='TotalCosts')
        self.df2.columns = ["TotalCost: " + x for x in self.df2.columns]

        # merge them into one single dataframe.
        self.df = self.df1.merge(self.df2,
                                left_index=True,
                                right_index=True,
                                how='left')
        
        #create a df that is from 1970-2015 - subset by index
        self.df = self.df.loc[1970:]
       
        # reset our dataframe to our output columns of choice.
        self.df = self.df[cols]
        
      
