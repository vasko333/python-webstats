from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    usename = models.CharField(max_length=120)
    password = models.CharField(max_length=120) 
