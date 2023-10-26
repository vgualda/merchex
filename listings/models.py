from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    title = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=32)


class Employee(models.Model):
    name = models.fields.CharField(max_length=100)
    registration = models.fields.IntegerField
    function = models.fields.CharField(max_length=64)
    department = models.fields.CharField(max_length=64)

#class Telephone(models.Model):
#    number = models.fields.CharField(max_length=14)


