from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.TimeField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
