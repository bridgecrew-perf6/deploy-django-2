from django.contrib import admin
from django.db.models.fields import PositiveBigIntegerField
from .models import Question, Choice, Login, Categories, Products
# Register your models here.


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Login)
admin.site.register(Categories)
admin.site.register(Products)