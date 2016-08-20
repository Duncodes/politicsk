from django.contrib import admin
from pkenya.diplomats.models import Regions

class RegionsAdmin(admin.ModelAdmin):
    list_display = ('name','deplomats',)
admin.site.register(Regions,RegionsAdmin)
