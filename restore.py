#!/usr/bin/python

import datetime
import subprocess
import re
import sys

#USAGE ./restore.py <app_url> <password> <dir>

APP = sys.argv[1]
PASSWORD = sys.argv[2]
DIR = sys.argv[3]

url_script = "echo %s | meteor mongo %s --url" % (PASSWORD, APP)
url = subprocess.check_output(url_script, shell=True);

m = re.search('mongodb://(.*):(.*)@(.*)/(.*)', url)

user = m.group(1)
password = m.group(2)
host = m.group(3)
database = m.group(4)

restore_script = 'mongorestore -u %s -h %s -d %s -p "%s" %s' % (user, host, database, password, DIR)

url = subprocess.check_call(restore_script, shell=True);