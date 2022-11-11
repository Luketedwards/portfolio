from django.db import models
import datetime

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(null=True, blank=True,)
    url = models.URLField(blank=True)
    date = models.DateTimeField(default='2012-06-30T20:00:00.000000000-0400', blank=True)
    image2 = models.ImageField(null=True, blank=True,)
    image3 = models.ImageField(null=True, blank=True,)
    image4 = models.ImageField(null=True, blank=True,)
    category = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=500, blank=True, null=True, default='')
    type = models.ForeignKey('typeOfApp', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(default='2012-06-30T20:00:00.000000000-0400', blank=True)

    def __str__(self):
        return self.name        


class typeOfApp(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type