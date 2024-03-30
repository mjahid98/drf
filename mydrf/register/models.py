from django.db import models

# Create your models here.
class user_register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=50)
    con_password = models.CharField(max_length=50)
