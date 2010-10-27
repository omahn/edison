from django.conf.urls.defaults import *
from piston.resource import Resource

from api.handlers import *

cfgitem_resource = Resource(handler=CfgItemHandler)
puppet_resource = Resource(handler=PuppetHandler)
package_resource = Resource(handler=PackageHandler)

urlpatterns = patterns('',
    url(r'^puppet/(?P<hostname>[^/]+)/$', puppet_resource), 
    url(r'^hosts/(?P<hostname>[^/]+)/$', cfgitem_resource), 
    # url(r'^auditorium/packages/(?P<id>\d+)$', package_resource),
    url(r'^auditorium/packages$', package_resource),
)

urlpatterns += patterns(
    'piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)

