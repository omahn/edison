from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout

# Project specific imports
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', home),
    # REST based API URI's
#    (r'^api/', include('edison.api.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
