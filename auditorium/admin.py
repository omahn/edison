# ensure that we include all the models required to administer this app
from models import *
from django.contrib import admin

admin.site.register(Package)
