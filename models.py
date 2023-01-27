from django.db import models
from django_cryptography.fields import encrypt
# Create your models here.
class order(models.Model):
    name=encrypt(models.CharField(max_length=20 ,null=True))
    number=encrypt(models.IntegerField(null=True))
    def __str__(self):
        return self.name