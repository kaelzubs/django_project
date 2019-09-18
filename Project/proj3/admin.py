from django.contrib import admin
from . models import Five_Page

# Register your models here.

class FiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
admin.site.register(Five_Page, FiveAdmin)
