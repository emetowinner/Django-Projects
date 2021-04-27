from django.contrib import admin
from . import models

admin.site.register(models.UserCase)
admin.site.register(models.UIProject)
admin.site.register(models.PersonalData)
admin.site.register(models.Assets)
