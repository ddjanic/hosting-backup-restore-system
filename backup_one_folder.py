#!/usr/bin/env python

import os
import tarfile
import time

# timestamp year - month - day
filestamp = time.strftime('%Y-%m-%d')

# paths where to store files .tar.gz
dr = "/mnt/share/backup/backup_ok/%s" % (filestamp)
if not os.path.exists(dr):
    os.makedirs(dr)
# need to backup /mnt/share/OK folder for example every 5 day days via cron
home = '/mnt/share/OK'

targ_file = dr+".tar.gz"

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

make_tarfile(targ_file, home)
