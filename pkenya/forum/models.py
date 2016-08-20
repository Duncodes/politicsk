from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from pkenya.messenger.models import Message

# Create your models here.
class Debate(models.Model):
    title=models.CharField(max_length=500)
    create_date=models.DateTimeField('Time of the Debate')
    completed_at=models.DateTimeField('Time Debate Ended',blank=True,null=True)
    invited=models.ForeignKey(User)

    def get_new_debates(self):
        now = timezone.now()
        latest=now - datetime.timedelta(days=1)
        return Debate.objects.filter(create_date=latest)
    def send_message_to_invited_user(self):
        current_user_message=Message.send_message(User.is_superuser,invited,"You are invited to a chat room")
        return current_user_message
