import MySQLdb as mdb
import sys

from settings import *

connection = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);
base_query = "select *, count(*), sum(price)/count(*) AS 'avg_price' from pricelist \
         where %s = '%s' AND listed_date >= '%s' AND listed_date <= '%s' \
         group by listed_date order by listed_date asc"

def fetchTrendsByQuery(query):
    """ fetch trends by query. """
    cur = connection.cursor()
    cur.execute(query)
    return cur.fetchall()    

def prepareTrendsQuery(queryCategory, queryId, startDt, endDt):
    """ """
    # todo : validate the parameters.
    return base_query % (queryCategory, queryId, startDt, endDt)

def fetchTrends(queryCategory, queryId, startDt, endDt):
    query = prepareTrendsQuery(queryCategory, queryId, startDt, endDt)
    trends = fetchTrendsByQuery(query)
    result = { "queryCategory" : queryCategory,
               "queryId" : queryId,
               "startDt" : startDt,
               "endDt"   : endDt,
               "trends"  : trends}
    return result

def printTrends(result):
    """ print trends in human readable format. """

    print "trends for %(queryCategory)s:%(queryId)s in range %(startDt)s to %(endDt)s" % (result)
    print "-" * 140
    trends = result["trends"]
    for trend in trends:
        print list(trend)
    print

if __name__ == '__main__':
    trends = fetchTrends('productId', '101332', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrends('categoryId', '3', '2012-02-06', '2012-02-29')
    printTrends(trends)

    trends = fetchTrends('brand', 'Sony', '2012-02-06', '2012-02-29')
    printTrends(trends)
    
