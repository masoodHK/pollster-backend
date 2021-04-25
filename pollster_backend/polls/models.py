import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from categories.models import Categories

# Create your models here.
class Poll(models.Model):
    question = models.CharField('Question for the polls',max_length=200)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1, related_name="polls")
    ends_on = models.DateTimeField()
    poll_type = models.CharField('Type of Poll', max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
    	return self.question

    def check_if_poll_ended(self):
    	now = timezone.now()
    	return self.ends_on <= now

class Section(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=1, null=True, blank=True)
    section_heading = models.CharField("The subquestion of the poll", max_length=300)

class Option(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option_text = models.CharField('The Text of the Option', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.option_text


class Comments(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    made_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    comment_text = models.CharField('The comment on the poll', max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
    	return self.comment_text