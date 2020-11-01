from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.StayHomeRecord)
admin.site.register(models.Location)
admin.site.register(models.Admin)
admin.site.register(models.Researcher)
admin.site.register(models.Tracer)
admin.site.register(models.Contact)
admin.site.register(models.Record)