#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleaning the dataset for Natural Disaster project
Will Johnson
10/24/21
"""

from NaturalDisastersDataCleaner import DisasterData


# pull our data, clean it, then save it to a new variable.
dataObj = DisasterData()
dataObj.cleanDf()
df = dataObj.df.copy()

# create a new csv with that dataset.
df.to_csv('../Data/Disasters_and_economic_impact_by_year.csv')
