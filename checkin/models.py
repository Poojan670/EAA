from django.db import models

# Create your models here.
class Entry(models.Model):
    name=models.CharField(max_length=50)
    secretkey=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    timein=models.DateTimeField(auto_now_add=True)
    timeout=models.DateTimeField(null=True)

class CheckEntry(models.Model):
    name=models.CharField(max_length=50)
    secretkey=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    timein=models.DateTimeField(auto_now_add=True)
    timeout=models.DateTimeField(null=True)
    

