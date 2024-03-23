from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class product(models.Model):
    product_title=models.CharField(max_length=50)
    product_feature=models.CharField(max_length=50)
    product_cost=models.CharField(max_length=50)
    product_link=models.CharField(max_length=50)
    product_img=models.FileField(upload_to="products/",max_length=250,null=True,default=None)
