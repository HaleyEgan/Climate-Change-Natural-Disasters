# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:17:13 2021

@author: dmd8a
"""

from NaturalDisastersDataCleaner import DisasterData



import unittest

class CorrectColumnsTest(unittest.TestCase):

    '''
    Here we are testing whether the cleanDf() function is actually deleting / retaining the correct columns.
    '''
    def test_deleted(self):
         check1 = DisasterData()
         check1.cleanDf() 
         self.assertNotIn('Earthquake',check1.df.columns) # or self.assertNotIn('Earthquake',self.final_columns)

    def test_retained(self):
         check2 = DisasterData()
         check2.cleanDf()
         self.assertIn('Extreme weather',check2.df.columns)

class ColumnsTypeTest(unittest.TestCase):

    '''check a column's data type, e.g. temperature is a float    '''

    def test_type(self):
        check3 = DisasterData()
        check3.cleanDf()
        self.assertEqual(check3.df['Extreme temperature'].dtypes, float)

    def test_type2(self):
        check4 = DisasterData()
        check4.cleanDf()
        self.assertEqual(check4.df['Extreme weather'].dtypes, float)


if __name__ == '__main__':
  unittest.main() 
         



