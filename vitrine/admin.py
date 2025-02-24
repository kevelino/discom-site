from django.contrib import admin
from .models import Contact, Service

class ContactAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'created_at')

admin.site.register(Contact, ContactAdmin)


class ServiceAdmin(admin.ModelAdmin):
  list_display = ('name', 'ref')

admin.site.register(Service, ServiceAdmin)
