from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout

# Project specific imports
from edison.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', home),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
