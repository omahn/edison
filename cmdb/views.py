# This file is part of the Edison Project.
# Please refer to the LICENSE document that was supplied with this software for information on how it can be used.
# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from models import *
from orchestra.models import *
from changemanagement.models import *
from auditorium.models import *

# Project specific imports
from models import *
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'edison',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


@login_required
def home(request):
    title = 'Configuration Database Home'
    section_item_name = 'Configuration Item'
    return render_to_response('cmdb/home.tpl',
            locals(),
            context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def listdata(request):
    link_desc = 'Configuration Item'
    cfgitems = ConfigurationItem.objects.all().order_by('Hostname')
    return render_to_response('cmdb/list.tpl',{'data_list':cfgitems,'link_desc':link_desc},context_instance=RequestContext(request)) #{'data_list':cfgitems,locals()})

@login_required
def asset(request,assetId):
	# get the details for the requested configurationItem
	cfgResult = ConfigurationItem.objects.select_related().filter(id=assetId)
	for cfgItem in cfgResult:
		# get the orchestra classes and Metadata
		orchestra_classes = OrchestraClass.objects.select_related('Name','Hostname').filter(AffectedItems__Hostname__icontains =  cfgItem.Hostname)
		orchestra_meta = OrchestraMetaDataValue.objects.select_related('Name','Hostname').filter(AffectedItems__Hostname__icontains =  cfgItem.Hostname)
		# Get any change requests linked to this item
		open_change_requests = ChangeHeader.objects.filter(AffectedItems__Hostname__icontains = cfgItem.Hostname,Completed = False).count()
		closed_change_requests = ChangeHeader.objects.filter(AffectedItems__Hostname__icontains = cfgItem.Hostname,Completed = True).count()
		# Get the total number of packages installed on this system according to Auditorium
		number_of_packages_installed = Package.objects.filter(AffectedItem__Hostname__icontains = cfgItem.Hostname).count()
		title = 'Asset Details for %s %s' % (cfgItem.Class.Name,cfgItem.Hostname)
		return render_to_response('cmdb/asset.tpl',
				{'data_list':cfgItem,
				'orchestra_classes':orchestra_classes,
				'orchestra_meta':orchestra_meta,
				'closed_change_requests':closed_change_requests,
				'open_change_requests':open_change_requests,
				'number_of_packages_installed': number_of_packages_installed,
				'title': title}
				,context_instance=RequestContext(request))

@login_required
def assetlist(request):
    cfgitems = ConfigurationItem.objects.all().order_by('Hostname')
    return render_to_response('cmdb/list.tpl',{'data_list':cfgitems,},context_instance=RequestContext(request)) #{'data_list':cfgitems,locals()})

