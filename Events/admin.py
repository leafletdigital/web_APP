from django.contrib import admin

from Events.models import events
class EventsAdmin(admin.ModelAdmin):
    list_display=("event_title","event_moto","event_desc","event_img")
# Register your models here.
admin.site.register(events,EventsAdmin)
# Register your models here.
