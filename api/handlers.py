from piston.handler import BaseHandler
from orchestra.models import *
from cmdb.models import *
from auditorium.models import *

class CfgItemHandler(BaseHandler):
	allowed_methods = ('GET')

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
		# Get a list of the configuration Management Classes
		classresults = OrchestraClass.objects.select_related('Name','Hostname').filter(AffectedItems__Hostname__icontains = hostname)
		classes = [] 
		for classresult in classresults: 
			classes.append(classresult.Name)
		data = {'classes' : classes}
		# get the metadata
		metadataresults = OrchestraMetaDataValue.objects.select_related('Name','Value','Hostname').filter(AffectedItems__Hostname__icontains = hostname)
		md = {}
		for mdresult in metadataresults:
			# The mdresult is a model so we need to convert it to a string
			md[str(mdresult.Name)] = mdresult.Value

		data['metadata'] = md
		return data

class PackageHandler(BaseHandler):
	model = Package

class LibVirtHandler(BaseHandler):
    allowed_methos = ('GET')

    def read(self,request,hostname):
        results = ConfigurationItem.objects.select_related().get(Hostname=hostname)
	serverDetails = results
	virtDetails = results.VMDefinition
	data = {'domain' : {'type' : virtDetails.VirtType, 'id' : serverDetails.id}, 'hostname' : serverDetails.Hostname}
	return data
