from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('library_identifier', 'email', 'first_name', 'last_name', 'created_at', 'updated_at')
