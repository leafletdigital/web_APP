from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    
    message = models.TextField()
# Create your models here.
