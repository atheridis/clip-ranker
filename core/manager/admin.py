from django.contrib import admin

# Register your models here.
from .models import Clip, ResetData

admin.site.register(Clip)
admin.site.register(ResetData)
