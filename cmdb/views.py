# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory


# Project specific imports
from models import *
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'Edison',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


@login_required
def home(request):
    title = 'Configuration Database Home'
    section_item_name = 'Configuration Item'
    return render_to_response('home.tpl',
            locals(),
            context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def listdata(request):
    link_desc = 'Configuration Item'
    cfgitems = ConfigurationItem.objects.all().order_by('Hostname')
    return render_to_response('list.tpl',{'data_list':cfgitems,'link_desc':link_desc,},context_instance=RequestContext(request)) #{'data_list':cfgitems,locals()})

@login_required
def edit(request,cfgid):
    title = 'Edit an Item'
    ItemFormSet = modelformset_factory(ConfigurationItem,max_num=1,extra=0)
    if request.method == 'POST':
        formset = ItemFormSet(request.POST, request.FILES)
	if formset.is_valid():
	   formset.save()
           request.user.message_set.create(message='The Configuration Item was updated sucessfully')
           return render_to_response('edit.tpl',context_instance=RequestContext(request, processors=[custom_proc]))
    else:
        formset = ItemFormSet()
	return render_to_response('edit.tpl', {"formset": formset,})
