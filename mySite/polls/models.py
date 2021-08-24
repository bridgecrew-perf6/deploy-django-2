from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.TimeField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)


class Login(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=255)

    def __str__(self) :
        return self.username


class Categories(models.Model):
    category_name = CharField(max_length=255)
    category_in = CharField(max_length=255,null=True)

class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = CharField(max_length=255)
    price = FloatField(default=0)
    discription = CharField(max_length=1000)
    url_images = CharField(max_length=1000)
    taitle = CharField(max_length=1000)
    status = BooleanField()


class Cart(models.Model):
    pass