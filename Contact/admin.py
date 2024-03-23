from django.contrib import admin
from Contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=("name","email","subject","message")
# Register your models here.
admin.site.register(Contact,ContactAdmin)
# Register your models here.
