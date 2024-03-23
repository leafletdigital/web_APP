from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class innovation(models.Model):
    innovation_title=models.CharField(max_length=50)
    innovation_desc=HTMLField()

    innovation_img=models.FileField(upload_to="innovations/",max_length=250,null=True,default=None)