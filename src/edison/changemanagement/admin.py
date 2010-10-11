# ensure that we include all the models required to administer this app
from edison.changemanagement.models import *
from django.contrib import admin

admin.site.register(ChangeHeader)
