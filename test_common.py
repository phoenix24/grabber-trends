#!/usr/bin/env python
"""
unit-tests for the common data fetch methods.
"""

import unittest
from common import *

class TestFetchTrends(unittest.TestCase):

    
    def test_fetch_trends_as_list1(self):
        expected = {'queryCategory': 'productId',
                    'endDt'  : '2012-02-09',
                    'startDt': '2012-02-06',
                    'queryId': '101332',
                    'trends' : [
                                 ['3', 'Mobile Phones', '101332', 'Alcatel OT 506D', 'Alcatel', '2012-02-06', '2', '3353.00'],
                                 ['3', 'Mobile Phones', '101332', 'Alcatel OT 506D', 'Alcatel', '2012-02-09', '4', '3353.00']
                               ]
                    }
        actual = fetchTrendsAsList('productId', '101332', '2012-02-06', '2012-02-09')
        self.assertEquals(expected, actual)

        
    def test_fetch_trends_as_list2(self):
        expected = {'queryCategory': 'categoryId', 'endDt': '2012-02-29', 'startDt': '2012-02-06', 'queryId': '3123', 'trends': []}
        actual = fetchTrendsAsList('categoryId', '3123', '2012-02-06', '2012-02-29')
        self.assertEquals(expected, actual)

        
    def test_fetch_trends_as_list3(self):
        expected = {'queryCategory': 'brand', 'endDt': '2012-02-29', 'startDt': '2012-02-06', 'queryId': 'Sony aasda', 'trends': []}
        actual = fetchTrendsAsList('brand', 'Sony aasda', '2012-02-06', '2012-02-29')
        self.assertEquals(expected, actual)

    
    def test_fetch_trends_as_dict1(self):
        expected = {'queryCategory': 'productId',
                    'endDt'  : '2012-02-09',
                    'startDt': '2012-02-06',
                    'queryId': '101332',
                    'trends' : [
                                {'category': 'Mobile Phones', 'count': '2', 'product': 'Alcatel OT 506D', 'brand': 'Alcatel', 'avg_price': '3353.00',
                                 'listed_date': '2012-02-06', 'categoryId': '3', 'productId': '101332'},
                                {'category': 'Mobile Phones', 'count': '4', 'product': 'Alcatel OT 506D', 'brand': 'Alcatel', 'avg_price': '3353.00',
                                 'listed_date': '2012-02-09', 'categoryId': '3', 'productId': '101332'}
                              ]
                    }
        actual = fetchTrendsAsDict('productId', '101332', '2012-02-06', '2012-02-09')
        self.assertEquals(expected, actual)

        
    def test_fetch_trends_as_dict2(self):
        expected = {'queryCategory': 'categoryId', 'endDt': '2012-02-29', 'startDt': '2012-02-06', 'queryId': '3123', 'trends': []}
        actual = fetchTrendsAsDict('categoryId', '3123', '2012-02-06', '2012-02-29')
        self.assertEquals(expected, actual)

        
    def test_fetch_trends_as_dict3(self):
        expected = {'queryCategory': 'brand', 'endDt': '2012-02-29', 'startDt': '2012-02-06', 'queryId': 'Sony aasda', 'trends': []}
        actual = fetchTrendsAsDict('brand', 'Sony aasda', '2012-02-06', '2012-02-29')
        self.assertEquals(expected, actual)
    

if __name__ == '__main__':
        unittest.main()

