from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.exceptions import ValidationError

class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    dateStart = models.DateField(default=timezone.now, editable=False)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(max_length=1024, blank=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=20, choices=[('1', 'Text'), ('2', 'Select'),
                                                    ('3', 'Select Multiple')], default='Select')

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024, null=True, blank=True)
    sChoice = models.ForeignKey(Choice, related_name='sChoice', on_delete=models.CASCADE, null=True, blank=True)
    mChoices = models.ManyToManyField(Choice, related_name='mChoices')

    def clean(self):
        super().clean()
        if self.sChoice is None and self.text and self.mChoices is None:
            raise ValidationError('Field text and choice are empty! '
                                  'Must be filled one of the choice')

    def __str__(self):
        return f'{self.question} - {self.sChoice or ""}{self.text or ""}{self.mChoices or ""}'
