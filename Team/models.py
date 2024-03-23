from django.db import models
class team(models.Model):
    team_link=models.CharField(max_length=50)
    team_img=models.FileField(upload_to="team/",max_length=250,null=True,default=None)
    member_name=models.CharField(max_length=100)
    member_twitter=models.CharField(max_length=100)
    member_facebook=models.CharField(max_length=100)
    member_instagram=models.CharField(max_length=100)
    member_linkedin=models.CharField(max_length=100)
# Create your models here.
