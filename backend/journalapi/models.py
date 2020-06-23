from django.db import models

# Create your models here.
class Journal(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=500)
    content=models.CharField(max_length=500)