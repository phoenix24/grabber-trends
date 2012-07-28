#!/bin/bash

if [ $# -ne 4 ] 
then
    echo "usage: ./setup.sh   <mysql user>  <mysql pass> <db-name> <path to data file>"
    exit
fi

# assign the args.
MYSQL_USER=$1
MYSQL_PASS=$2
MYSQL_DB_NAME=$3
DATA_FILE_PATH=$4

# create the table for the price catalog.
CREATE_TABLE="create table pricelist
              (categoryId int not null, category varchar(256), productId int not null, product varchar(256), price int, retailer varchar(256), listed_date DATE, brand varchar(256));"

echo "create table."
mysql -u $MYSQL_USER -p$MYSQL_PASS $MYSQL_DB_NAME -e "$CREATE_TABLE"



# load the raw file into the database table (and skip header).
LOAD_TABLE="load data local infile '$DATA_FILE_PATH' 
            into table pricelist fields terminated by ',' enclosed by '\"' lines terminated by '\n' ignore 1 lines (categoryId, category, productId, product, price, retailer, listed_date, brand);"

echo "load data file to the table"
mysql -u $MYSQL_USER -p$MYSQL_PASS $MYSQL_DB_NAME -e "$LOAD_TABLE"

