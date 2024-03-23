from django.contrib import admin
from Values.models import values
class ValueAdmin(admin.ModelAdmin):
    list_display=("values_No","values_title","values_desc")
# Register your models here.
admin.site.register(values,ValueAdmin)
