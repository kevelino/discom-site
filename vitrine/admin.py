from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
  list_display = ('name', 'ref')

admin.site.register(Service, ServiceAdmin)
