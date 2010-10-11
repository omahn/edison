# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Project specific imports
from edison.cmdb.models import *

@login_required
def home(request):
    return HttpResponse('Configuration Management Database home page')

