from piston.handler import BaseHandler
from edison.cmdb.models import ConfigurationItem

class CfgItemHandler(BaseHandler):
	allowed_methods = ('GET',)
	fields = ('Hostname','Rack','Asset','DataCentre')
	model = ConfigurationItem


	def read(self,request,hostname):
		data = ConfigurationItem.objects.get(Hostname=hostname)
		return data
