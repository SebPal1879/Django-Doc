import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    question_text = models.CharField("Question text",max_length=200)#By setting the first positional argument, a name is given to the field which works as documentation
    pub_date = models.DateTimeField("Date published")
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
    