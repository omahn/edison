from django.conf.urls.defaults import *
from piston.resource import Resource

from edison.api.handlers import CfgItemHandler

cfgitem_resource = Resource(handler=CfgItemHandler)

urlpatterns = patterns('',
    url(r'^hosts/(?P<hostname>[^/]+)/$', cfgitem_resource), 
)
