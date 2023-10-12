from django.contrib import admin
from .models import TreeMenu


class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'path', 'parent', 'table_name']
    fields = ['name', 'parent', 'table_name']

admin.site.register(TreeMenu, TreeMenuAdmin)