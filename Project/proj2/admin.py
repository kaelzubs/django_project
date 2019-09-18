from django.contrib import admin
from . models import Three_Page

# Register your models here.

class ThreeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
admin.site.register(Three_Page, ThreeAdmin)
