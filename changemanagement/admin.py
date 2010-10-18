# ensure that we include all the models required to administer this app
from models import *
from django.contrib import admin

admin.site.register(ChangeHeader)
admin.site.register(ChangeStatus)
admin.site.register(Details)
admin.site.register(ScmRepo)
admin.site.register(Scmtype)
