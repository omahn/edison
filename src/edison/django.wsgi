import os
import sys

# update this variable to point to your edison installation
#
# EXAMPLE:
# 
# if your site is in /var/djangosites/edison then this needs to be set to '/var/djangosites/'
edisonhome = '/var/djangosites/'


sys.path.append(edisonhome)
sys.path.append(edisonhome + 'edison/src/')
sys.path.append(edisonhome + '/edison/src/edison/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'edison.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
