#!/usr/bin/env python

import os
import tarfile
import time

filestamp = time.strftime('%Y-%m-%d')

# paths
dr = "/home/backup/www/%s" % (filestamp)
if not os.path.exists(dr):
    os.makedirs(dr)

home = '/var/www/'
backup_dir = dr

home_dirs = [ name for name in os.listdir(home) if os.path.isdir(os.path.join(home, name)) ]

for directory in home_dirs:
    full_dir = os.path.join(home, directory)
    tar = tarfile.open(os.path.join(backup_dir, directory+'.tar.gz'), 'w:gz')
    tar.add(full_dir)
    tar.close()
