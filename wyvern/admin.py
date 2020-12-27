from django.contrib import admin

from .models import Client, Kind

admin.site.register(Client)
admin.site.register(Kind)

