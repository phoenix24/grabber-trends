#!/usr/bin/env python

from settings import *
import MySQLdb as mdb

connection = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);
base_query = "select categoryId, category, productId, product, brand, listed_date, count(*) as count, sum(price)/count(*) AS 'avg_price' from pricelist \
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
