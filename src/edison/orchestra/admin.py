# ensure that we include all the models required to administer this app
from edison.orchestra.models import *
from django.contrib import admin

admin.site.register(OrchestraClass)
admin.site.register(OrchestraMetaDataName)
admin.site.register(OrchestraMetaDataValue)
