from __future__ import unicode_literals
from django.db import models
from graphene import ObjectType, String, ID, Boolean, Int, Field


# Create your models here.
class Repo(models.Model):
    name = models.TextField()
    description = models.TextField()
    url = models.TextField()

# class Owner(models.Model):
#     login = models.TextField()
#     avatar_url = models.TextField()
#     followers_url = models.TextField()
#     repo = models.ForeignKey(Repo, on_delete=models.CASCADE)
	


