#!/bin/bash
set -e
service mysql start
mysql < /mysql/setup.sql
service mysql stop
##!/bin/bash
#mysql --user=$MYSQL_USER --password=MYSQL_PASSWORD < /db/kaiserhofinfovis.sql

