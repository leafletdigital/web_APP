from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class events(models.Model):
    event_title=models.CharField(max_length=50)
    event_moto=models.CharField(max_length=50)
    event_desc=HTMLField()

    event_img=models.FileField(upload_to="events/",max_length=250,null=True,default=None)

# Create your models here.
