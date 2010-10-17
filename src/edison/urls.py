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
    # REST based API URI's
    (r'^api/', include('edison.api.urls')),
    (r'^cmdb/', include('edison.cmdb.urls')),
    (r'^changemanagement/', include('edison.changemanagement.urls')),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/$', home),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
