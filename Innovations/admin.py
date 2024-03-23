from django.contrib import admin
from Innovations.models import innovation
class InnovationAdmin(admin.ModelAdmin):
    list_display=("innovation_title","innovation_desc","innovation_img")
# Register your models here.
admin.site.register(innovation,InnovationAdmin)