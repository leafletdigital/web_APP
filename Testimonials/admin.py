from django.contrib import admin
from Testimonials.models import testimonila
class TestiminilaAdmin(admin.ModelAdmin):
    list_display=("testimonila_title",)
# Register your models here.
admin.site.register(testimonila,TestiminilaAdmin)
# Register your models here.
