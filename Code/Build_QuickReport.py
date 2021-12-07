import pandas as pd
from quickda.explore_data import *

#load dataset
df = pd.read_csv('../Data/Disasters_and_economic_impact_by_year.csv')

# build our report HTML file. 
explore(df, method='profile',report_name='Report: Disasters and Economic Impact by Year')
