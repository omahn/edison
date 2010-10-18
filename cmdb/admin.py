# ensure that we include all the models required to administer this app
from edison.cmdb.models import *
from django.contrib import admin

admin.site.register(ConfigurationItem)
admin.site.register(ConfigurationItemClass)
admin.site.register(NetworkInterface)
admin.site.register(DataCentreRack)
admin.site.register(DataCentreSuite)
admin.site.register(DataCentreRoom)
admin.site.register(DataCentre)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(County)
admin.site.register(Country)
