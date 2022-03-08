from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField


# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(default=False, null=True)

    def __str__(self) :
        return self.username
    


class Categories(models.Model):
    category_name = CharField(max_length=255)
    category_in = CharField(max_length=255,null=True)
    
    def __str__(self) :
        return self.category_name

class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = CharField(max_length=255)
    price = FloatField(default=0, null=True, blank=True)
    discription = CharField(max_length=1000, null=True)
    url_images = CharField(max_length=1000, null=True)
    title = CharField(max_length=1000, null=True)
    status = BooleanField()

    def __str__(self) :
        return self.product_name


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    username = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self) :
        return self.username.username