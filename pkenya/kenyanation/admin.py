from django.contrib import admin


from . models import PolicalPatie

class PolicalPatieAdmin(admin.ModelAdmin):
    list_display=('name','chair','year')

admin.site.register(PolicalPatie,PolicalPatieAdmin)
