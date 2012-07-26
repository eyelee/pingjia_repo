from django.db import models
from scrapy.item import Field
from scrapy.contrib_exp.djangoitem import DjangoItem

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    
class PersonItem(DjangoItem):
    django_model = Person

class PItem(DjangoItem):
    django_model = Person
    sex = Field()
    
class Pname(DjangoItem):
    django_model = Person
    name = Field(default='No Name')


# Create your models here.
