from django.db import models
from  django.contrib.auth.models import User




class Product(models.Model):
    author_product = models.ForeignKey(User, on_delete=models.PROTECT)
    name_product = models.CharField(max_length=100)
    time_started = models.DateTimeField(auto_now=True)
    price_product = models.IntegerField()

    def __str__(self) -> str:
        return self.name_product
    

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name_lesson = models.CharField(max_length=100)
    video = models.URLField(max_length=500)
    
    def __str__(self) -> str:
        return self.name_lesson

class Group(models.Model):
    users = models.ManyToManyField(User)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    name_group = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name_group

    