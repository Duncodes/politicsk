from django.db import models
from django.contrib.auth.models import User

class Regions(models.Model):
    name=models.CharField(max_length=20)
    deplomats=models.ForeignKey(User)
