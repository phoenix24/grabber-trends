#!/usr/bin/env python

import sys
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


def usage():
    print "usage instructions    :"
    print
    print "\t$ python pricetrends_cmd.py  <trend-type> <id or name of product>  <stard-dt> <end-dt>"
    print "\t<trend-type>           , should be one of the following  : productId/categoryId/brand"
    print "\t<id or name of product>, depending on trend type this should be one of the following : productID/categoryID/brandName"
    print "\t<startDt>              , valid start date in (YYYY-MM-DD Format)"
    print "\t<endDt>                , valid end date in (YYYY-MM-DD Format)"
    sys.exit(1)


def validateArgs(qtype, qid, stdate, enddate):
    
    if qtype not in ["productId", "categoryId", "brand"]:
        print "ERROR : invalid trend query type. Try Again!"
        sys.exit(-1)

    #todo
    # if stdate:
    #     print "ERROR : invalid trend query type."
    
    # if enddate:
    #     print "ERROR : invalid trend query type."
    
    
if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print usage()


    # 'categoryId', '3123', '2012-02-06', '2012-02-29'
    # 'productId', '101332', '2012-02-06', '2012-02-29'
    # 'brand', 'Sony aasda', '2012-02-86', '2012-02-29'

    qtype, qid, stdate, enddate = sys.argv[1:]
    validateArgs(qtype, qid, stdate, enddate)

    trends = fetchTrendsAsList('productId', '101332', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrendsAsList('categoryId', '3123', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrendsAsList('brand', 'Sony aasda', '2012-02-86', '2012-02-29')
    printTrends(trends)
    
