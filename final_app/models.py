# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    image = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
