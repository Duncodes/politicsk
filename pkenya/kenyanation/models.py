from django.db import models
from django.contrib.auth.models import User

class PolicalPatie(models.Model):
    name=models.CharField(max_length=20)
    chair=models.ForeignKey(User)
    year=models.DateTimeField('When formed')
    description=models.TextField()
