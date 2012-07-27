#!/usr/bin/env python

from settings import *
import MySQLdb as mdb

connection = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);
field_query = ["categoryId", "category", "productId", "product", "brand", "listed_date", "count", "avg_price"]
base_query = "select categoryId, category, productId, product, brand, listed_date, count(*), round(sum(price)/count(*), 2) from pricelist \
         where %s = '%s' AND listed_date >= '%s' AND listed_date <= '%s' \
         group by listed_date order by listed_date asc"

def fetchTrendsByQuery(query):
    """ fetch trends by query. """
    cur = connection.cursor()
    cur.execute(query)
    return cur.fetchall()    

def prepareTrendsQuery(queryCategory, queryId, startDt, endDt):
    """ prepare sql query that'll fetch trends. """
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

def fetchTrendsAsDict(queryCategory, queryId, startDt, endDt):
    """ return trends as dict. """
    result = fetchTrends(queryCategory, queryId, startDt, endDt)
    trends = result["trends"]

    ntrends = []
    for trend in trends:
        ntrend = dict(zip(field_query, trend))
        ntrends.append(ntrend)

    result["trends"] = ntrends
    return result

def fetchTrendsAsList(queryCategory, queryId, startDt, endDt):
    """ return trends as a list. """
    result = fetchTrends(queryCategory, queryId, startDt, endDt)
    trends = result["trends"]

    ntrends = []
    for trend in trends:
        ntrend = map(str, trend)
        ntrends.append(ntrend)

    result["trends"] = ntrends
    return result
