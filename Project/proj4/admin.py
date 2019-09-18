from django.contrib import admin
from . models import Ten_Page

# Register your models here.

class TenAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
admin.site.register(Ten_Page, TenAdmin)
