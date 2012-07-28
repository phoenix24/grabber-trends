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

