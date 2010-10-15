from django.conf.urls.defaults import *
from piston.resource import Resource

from edison.api.handlers import *

cfgitem_resource = Resource(handler=CfgItemHandler)
puppet_resource = Resource(handler=PuppetHandler)

urlpatterns = patterns('',
    url(r'^puppet/(?P<hostname>[^/]+)/$', puppet_resource), 
    url(r'^hosts/(?P<hostname>[^/]+)/$', cfgitem_resource), 
)
