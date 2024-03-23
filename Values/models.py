from django.db import models
from tinymce.models import HTMLField
class values(models.Model):
    values_No=models.CharField(max_length=50)
    values_title=models.CharField(max_length=100)
    values_desc=HTMLField()

# Create your models here.
