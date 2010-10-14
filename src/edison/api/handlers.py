from piston.handler import BaseHandler
from edison.cmdb.models import *

class CfgItemHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('Hostname',('Rack',('Suite',('Room',(),),),),'Asset','DataCentre')
	model = ConfigurationItem,DataCentreRack,DataCentreSuite,DataCentreRoom


	def read(self,request,hostname):
		data = ConfigurationItem.objects.get(Hostname=hostname)
		return data
