#!/usr/bin/env python3
import sys, os, os.path, glob, shutil
import subprocess, argparse
import getpass
import datetime


RSYNC_OPTIONS = [
  '-e "ssh -p 9988"',
#  '--verbose',
  '--stats',
  '--delete',
  '--links',
  '--checksum',
  '--recursive',
  '--compress',
  '--perms',
  '--owner',
  '--group',
  '--times',
]



# set up the destination
DEST_HOST, DEST_DIR = ( 'test.myeducator.com', '/home/lexicity/')

# ensure the user really wants to do this
areyousure = input("Are you sure you are ready to upload to the %s site? (y/n) " % DEST_HOST)

if areyousure.lower() != 'y':
  print('Canceled.')
  sys.exit(0)


# initialize django so we can use the settings and anything else
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
  

######################################################################################################################
###   Collect and minify the static files

print('Collecting and minifying static files...')
# delete the minified directory
if os.path.exists(settings.STATIC_ROOT):
  shutil.rmtree(settings.STATIC_ROOT)
# run the collect static command
os.system('python3 manage.py dmp_collectstatic')

  


#####################################################
###  Upload to the server

# erase the local template cache and *.pyc files
print('Removing temporary files...')
for cmd in [
  "find . -name 'cached_templates' -exec /bin/rm -rf {} \;",
  "find . -name '__pycache__' -exec /bin/rm -rf {} \;",
]:
  os.system(cmd)
 
# stop the web server
print("Stopping web server...")
os.system('''ssh -p 9988 root@%s " /etc/init.d/nginx stop; /etc/init.d/uwsgi stop;"''' % (DEST_HOST))

# copy over everything
print('Comparing and copying files to the server...')
cmd = 'rsync %s %s root@%s:%s' % (' '.join(RSYNC_OPTIONS), os.path.join(settings.BASE_DIR, '*'), DEST_HOST, DEST_DIR)
print(cmd)
os.system(cmd)

# erase the *.pyc files and template_cache so python/Mako recompiles everything on the web site
print('Emptying the dev server caches...')
rmcmds = [ 'rm -rf %s;' % os.path.join(DEST_DIR, appname, 'cached_templates') for appname in settings.CUSTOM_APPS ]
os.system('''ssh -p 9988 root@%s "%s"''' % (DEST_HOST, ' '.join(rmcmds)))
os.system('''ssh -p 9988 root@%s "find %s -name '*.pyc' -exec rm -rf {} \;"''' % (DEST_HOST, DEST_DIR))

# change user permissions
print('Settings permissions...')
os.system('''ssh -p 9988 root@%s "chown -R www-data:www-data %s;"''' % (DEST_HOST, DEST_DIR))

# reboot the web server
print("Restarting web server")
os.system('''ssh -p 9988 root@%s "cd %s; /etc/init.d/uwsgi restart; /etc/init.d/nginx restart;"''' % (DEST_HOST, DEST_DIR))


