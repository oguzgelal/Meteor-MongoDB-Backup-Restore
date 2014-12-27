#!/usr/bin/python

import datetime
import subprocess
import re
import sys

#USAGE ./backup.py <app_url> <password>

APP = sys.argv[1]
PASSWORD = sys.argv[2]

url_script = "echo %s | meteor mongo %s --url" % (PASSWORD, APP)
url = subprocess.check_output(url_script, shell=True);

m = re.search('mongodb://(.*):(.*)@(.*)/(.*)', url)

user = m.group(1)
password = m.group(2)
host = m.group(3)
database = m.group(4)

today = datetime.datetime.now()
output_dir = today.strftime("backup-%d_%m_%Y-%H_%M_%S")

backup_script = 'mongodump -h %s -u %s -p %s -d %s -o %s' % \
    (host, user, password, database, output_dir)
url = subprocess.check_call(backup_script, shell=True);