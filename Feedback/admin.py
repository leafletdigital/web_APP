from django.contrib import admin

from Feedback.models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","date","message")
# Register your models here.
admin.site.register(Feedback,FeedbackAdmin)
# Register your models here.