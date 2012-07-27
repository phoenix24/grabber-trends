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


def productTrendsById(productId, startDt, endDt):
    """ fetch product trends for the startDt and endDt. """

    query = base_query % ('productId', productId, startDt, endDt)
    return fetchTrendsByQuery(query)


def categoryTrendsById(productId, startDt, endDt):
    """ fetch category trends for the startDt and endDt. """

    query = "select *, count(*), sum(price)/count(*) AS 'avg_price' from pricelist \
             where categoryId = '%s' AND listed_date >= '%s' AND listed_date <= '%s' \
             group by listed_date order by listed_date asc"  % (productId, startDt, endDt)

    return fetchTrendsByQuery(query)


def brandTrendsByName(productId, startDt, endDt):
    """ fetch category trends for the startDt and endDt. """

    query = "select *, count(*), sum(price)/count(*) AS 'avg_price' from pricelist \
             where brand = '%s' AND listed_date >= '%s' AND listed_date <= '%s' \
             group by listed_date order by listed_date asc"  % (productId, startDt, endDt)

    return fetchTrendsByQuery(query)


def printTrends(trends):
    """ print trends in human readable format. """
    for trend in trends:
        print trend


if __name__ == '__main__':
    trends = productTrendsById('101332', '2012-02-06', '2012-02-29')
    printTrends(trends)

    # print
    # trends = categoryTrendsById('1', '2012-02-06', '2012-02-29')
    # printTrends(trends)
    
    # print
    # trends = brandTrendsByName('Alcatel', '2012-02-06', '2012-02-29')
    # printTrends(trends)
    
