#!/usr/bin/env python

from common import *

def printTrends(result):
    """ print trends in human readable format. """

    header = "trends for %(queryCategory)s:%(queryId)s in range %(startDt)s to %(endDt)s" % (result)
    footer = "-" * len(header)

    # do the printing!
    print header
    print footer
    for trend in result["trends"]:
        print '|'.join(trend)
    print footer
    print
    
if __name__ == '__main__':
    trends = fetchTrendsAsList('productId', '101332', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrendsAsList('categoryId', '3123', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrendsAsList('brand', 'Sony aasda', '2012-02-86', '2012-02-29')
    printTrends(trends)
    
