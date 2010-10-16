import os
import sys

sys.path.append('/var/djangosites/')
sys.path.append('/var/djangosites/edison/src/')
sys.path.append('/var/djangosites/edison/src/edison/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'edison.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
