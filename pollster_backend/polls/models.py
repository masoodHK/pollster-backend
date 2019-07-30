import datetime

from django.db import models
from django.utils import timezone

from categories.models import Categories

# Create your models here.
class Poll(models.Model):
    question = models.CharField('Question for the poll',max_length=200)
    is_active = models.BooleanField(default=True)
    ends_on = models.DateTimeField()
    poll_type = models.CharField('Type of Poll', max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
    	return self.question

    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.date_created <= now

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option_text = models.CharField('The Text of the Option', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.option_text


class Comments(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    comment_text = models.CharField('The comment on the poll', max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.comment_text