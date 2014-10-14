#!/usr/bin/env python

import os
import time
import gzip

filestamp = time.strftime('%Y-%m-%d')

# paths
dr = "/home/backup/cfg/%s" % (filestamp)
if not os.path.exists(dr):
    os.makedirs(dr)

# cfg path
mysql = "/etc/mysql/my.cnf"
apache2 = "/etc/apache2/apache2.conf"
sites = "/etc/apache2/sites-available/default"
php = "/etc/php5/apache2/php.ini"
samba = "/etc/samba/smb.conf"

# cfg list


f_in = open(mysql, 'rb')
f_out = gzip.open(dr+'/my.cnf.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f_in = open(apache2, 'rb')
f_out = gzip.open(dr+'/apache2.conf.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f_in = open(sites, 'rb')
f_out = gzip.open(dr+'/default.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f_in = open(php, 'rb')
f_out = gzip.open(dr+'/php.ini.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f_in = open(samba, 'rb')
f_out = gzip.open(dr+'/smb.conf.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()



