from django.db import models
from  django.contrib.auth import User
from  django.contrib.auth.mixins import LoginRequiredMixin




class Product(models.Model):
    author_product = models.ForeignKey(User, on_delete=models.PROTECT)
    name_product = models.CharField(max_length=100)
    time_started = models.DateTimeField(auto_now=True)
    price_product = models.IntegerField()

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name_lesson = models.CharField(max_length=100)
    video = models.URLField(max_length=500)


class Group(models.Model):
    users = models.ManyToManyField(User,related_name='groups')
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    name_group = models.CharField(max_length=100)


    