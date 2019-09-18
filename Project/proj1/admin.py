from django.contrib import admin
from . models import Home_Page

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
admin.site.register(Home_Page, HomeAdmin)
