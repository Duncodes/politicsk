from django.db import models
from . import list_themes
class themeModels(models.Model):
    theme=models.CharField(max_length=255,default='dafault',choices=list_themes())
