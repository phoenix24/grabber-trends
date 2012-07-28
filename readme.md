price trends analyzer.
===============================



##### pre-requsites
-------------------------------
- mysql as the data-store. (haven't used in a long time now!)
- bash, ubuntu 10.10 +


##### setup
-------------------------------
- create a database.
- create datatable, load the database.
- $ sh ./setup.sh db-user db-pass db-name /path/to/price.csv 


##### solution1, poor man's solution.
-------------------------------
- query trends over the commandline., usage details -

$ python pricetrends_cmd.py  <trend-type> <id or name of product>  <stard-dt> <end-dt>"
         <trend-type>           , should be one of the following  : productId/categoryId/brand"
         <id or name of product>, depending on trend type this should be one of the following : productID/categoryID/brandName"
         <startDt>              , valid start date in (YYYY-MM-DD Format)"
         <endDt>                , valid end date in (YYYY-MM-DD Format)"


sample arguments - 
$ python pricetrends_cmd.py categoryId 3 2012-02-06 2012-02-29"
$ python pricetrends_cmd.py productId 101332 2012-02-06 2012-02-29"
$ python pricetrends_cmd.py brand Sony aasda 2012-02-86 2012-02-29"


##### solution2, rich man's solution.
-------------------------------
- query trends over the web ui.
- start the server by kicking off ./pricetrends_web.py
- you'll get a local web-server running on port 10000



##### Scaling Price Trends Applicaiton
------------------------------------------------
Database is the bottleneck in such an application, where we do almost no data manipulation in the application logic., That said, we should direct majority of our efforts in optimizing db-performance.

Here's an idea, if we were to use mysql for production uses - 

One of the first things would be to pre-compute the average prices based on these three dimensions, and not compute them over and over again for each request (as in the current implementation).

Another thing to increase response would be to store a lot of these price trends in the in-memory databases, such as redis/memcache. I prefer redis-cluster, which also has recently added a beta 
version of the failover management.

For massively large price datasets, I would recommend not adding db-normalization for the disk-space savings may negatively impact the data-access retrival rates.
Also, another thing would be to horizontally shard the database based on the categorys., such that even in the case where we encounter a cache-miss having used a sharded database we'll 
need to specifically search/compute only in one/two unique shards.

Finally, some natural optimizations include adding primary keys and indexing based on them; so as to enhance read thruput.




##### Design Documentation
-------------------------------
Heart of the application logic lies in common.py, which implements a few fetchTrends methods; fetchTrendsAsList and fetchTrendsAsDict.
- fetchTrendsAsList - is a wrapper method, that returns trends as list, is used by the commandline program.
- fetchTrendsAsDict - is a wrapper method, that returns trends as dict, to used by the web ui, where the dict would be translated as a JSON for UI Charts input.

Both of these above methods, are build on top of fetchTrends method, which adds meta-data to the result; meta data such as - startDt/endDate/queryId etc.
Above method fetchTrends uses prepareTrendsQuery and fetchTrendsByQuery to prepare the query for the said trends query arguments.

pricetrends_cmd implentends argument parsing, argument validation and printing the trends recieved in a neat/clean human readable form.

Also, a good starting point to read the code would be test_common.py, it implements simple unit tests for the fetchTrendsAsList and fetchTrendsAsDict methods.
Although these tests are not extensive in their coverage and neither work isolated to the database, that's easy to implement and was intentially skipped due to bad health.

Note, you'll find relavant documentation blocks as part of the method implementations.
