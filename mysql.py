#!/usr/bin/env python

import ConfigParser
import os
import time

# conf
config = ConfigParser.ConfigParser()
config.read("/etc/mysql/debian.cnf")
username = 'user'
password = 'passwd'
hostname = 'localhost'

filestamp = time.strftime('%Y-%m-%d')

# paths
dr = "/home/backup/sql/%s" % (filestamp)
if not os.path.exists(dr):
    os.makedirs(dr)
# db list
database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if database == 'information_schema':
        continue
    if database == 'performance_schema':
        continue
    filename = "/home/backup/sql/%s/%s_%s.sql" % (filestamp, database, filestamp)
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s --skip-lock-tables | gzip -c > %s.gz" % (username, password, hostname, database, filename))
