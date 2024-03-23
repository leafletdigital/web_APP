from django.db import models
class gallery(models.Model):
    gallery_img=models.FileField(upload_to="gallery/",max_length=250,null=True,default=None)
# Create your models here.
