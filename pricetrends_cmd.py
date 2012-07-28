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
    print
    print "\t# sample usage : "
    print "\t$ python pricetrends_cmd.py categoryId 3 2012-02-06 2012-02-29"
    print "\t$ python pricetrends_cmd.py productId 101332 2012-02-06 2012-02-29"
    print "\t$ python pricetrends_cmd.py brand Sony aasda 2012-02-86 2012-02-29"
    print
    sys.exit(1)


def validateArgs(qtype, qid, stdate, enddate):
    return True

    #todo
    # if invalidDate(stdate) or invalidDate(stdate) or invalidQtype(qtype):
    #     print "ERROR : invalid trend query type."
    
    
if __name__ == '__main__':
    
    if len(sys.argv) != 5:
        print usage()

    qtype, qid, stdate, enddate = sys.argv[1:]
    validateArgs(qtype, qid, stdate, enddate)

    # fetch trends for the arguments and print them.
    trends = fetchTrendsAsList(qtype, qid, stdate, enddate)
    printTrends(trends)
    
