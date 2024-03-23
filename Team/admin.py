from django.contrib import admin
from Team.models import team
class TeamAdmin(admin.ModelAdmin):
    list_display=("team_link","team_img","member_twitter","member_facebook","member_instagram","member_linkedin")

admin.site.register(team,TeamAdmin)
# Register your models here.
