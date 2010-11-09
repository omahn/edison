# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
import re
from piston.handler import BaseHandler
from orchestra.models import *
from cmdb.models import *
from auditorium.models import *

# function to replace words in a given string of text
# copied shamelessly from http://www.daniweb.com/forums/thread70426.html

def replace_words(text, word_dic):
	"""
	take a text and replace words that match a key in a dictionary with
	the associated value, return the changed text
	"""
	rc = re.compile('|'.join(map(re.escape, word_dic)))
	def translate(match):
        	return word_dic[match.group(0)]
	return rc.sub(translate, text)


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
    allowed_methods = ('GET')

    def read(self,request,hostname):
        results = ConfigurationItem.objects.select_related().get(Hostname=hostname)
	serverDetails = results
	virtDetails = results.VMDefinition
	data = {'domain': {'type' : virtDetails.VMType, 'id' : serverDetails.id}, 'hostname' : serverDetails.Hostname}
	return data

class KickstartHandler(BaseHandler):
    allowed_methods = ('GET')
    def read(self,request):
	profile = ""
	mac = request.META["HTTP_X_RHN_PROVISIONING_MAC_0"].split(" ")
	profile = "Mac Address: " + mac[1] + "\n"
	results = ConfigurationItem.objects.select_related().filter(NetworkInterface__MacAddress__icontains=mac[1],BuildOnNextBoot=True)
	for data in results:
            # A Dict containing the defaults for the basic kickstart templating
            ksvars = {
                       '<<hostname>>': data.Hostname , # defaults to hostname retrieved for this MAC Address
		       "<<tree>>":"http://"+request.META['SERVER_NAME']+"/cmdb/installtree/"+data.Hostname, # Defaults to the Edison server and cmdb view
		       "<<rootpw>>":data.rootpwhash,
		       '<<bootdev>>': mac[1],
		      }
            profile = replace_words(data.Profile.AutoInstallFile,ksvars)
	return profile
