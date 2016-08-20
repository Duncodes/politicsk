from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor


class Page(models.Model):
    title=models.CharField(max_length=500)
    service=FroalaField(plugins=('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
            'entities', 'file', 'font_family', 'font_size',     'image_manager', 'image', 'inline_style','fullscreen',
            'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
            'url', 'video'),theme='dark')
    mission=models.CharField(max_length=500)
    vission=models.CharField(max_length=500)
    team=models.TextField()
    pub_date=models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class FundRaisingPage(models.Model):
    title=models.CharField(max_length=500)
    service=FroalaField(plugins=('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
            'entities', 'file', 'font_family', 'font_size',     'image_manager', 'image', 'inline_style','fullscreen',
            'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
            'url', 'video'),theme='dark')
    location=models.CharField(max_length=500)
    Ammounttoraise=models.CharField(max_length=400)
    date=models.DateTimeField('Date of Events',auto_now_add=True)

class Events(models.Model):
    title=models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    people=models.ForeignKey(User)

class PowerTable(models.Model):
    title=models.CharField(max_length=500)
    
    held_time=models.DateTimeField('Date of event')
