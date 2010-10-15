from piston.handler import BaseHandler
from edison.orchestra.models import *
from edison.cmdb.models import *

class CfgItemHandler(BaseHandler):
	allowed_methods = ('GET',)

	def read(self,request,hostname):
		results = ConfigurationItem.objects.select_related().get(Hostname=hostname)
		serverDetails = results
		locationDetails = results.Rack
		data = {'hostname' : serverDetails.Hostname, \
		'dc_rack' : locationDetails.RackName, \
		'dc_suite' : locationDetails.Suite.SuiteName, \
		'dc_room': locationDetails.Room.RoomName, \
		'datacentre' : locationDetails.Room.DataCentre.Name, \
		'item_class': serverDetails.Class.Name}
		return data

class PuppetHandler(BaseHandler):
	allowed_methods = ('GET')

	def read(self,request,hostname):
		results = OrchestraClass.objects.select_related('Name','Hostname').filter(AffectedItems__Hostname__icontains = hostname)
		data = [] 
		for result in results: 
			data.append(result.Name)
		return data
