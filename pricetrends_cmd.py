#!/usr/bin/env python

from common import *

def printTrends(result):
    """ print trends in human readable format. """

    header = "trends for %(queryCategory)s:%(queryId)s in range %(startDt)s to %(endDt)s" % (result)
    footer = "-" * len(header)
    print header
    print footer
    trends = result["trends"]
    for trend in trends:
        print list(trend)
    print footer
    print
    
if __name__ == '__main__':
    trends = fetchTrends('productId', '101332', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrends('categoryId', '3', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrends('brand', 'Sony', '2012-02-06', '2012-02-29')
    printTrends(trends)
    
