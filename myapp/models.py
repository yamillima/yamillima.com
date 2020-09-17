from django.db import models


# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
