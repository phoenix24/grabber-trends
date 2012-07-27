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
- $ ./setup.sh <db-name>


##### solution1, poor man's solution.
-------------------------------
- query trends over the commandline.
- $ ./pricetrends_cmd.py


##### solution2, rich man's solution.
-------------------------------
- query trends over the web ui.
- start the server by kicking off ./pricetrends_web.py
- you'll get a local web-server running on port 10000

