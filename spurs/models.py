from django.db import models

# Create your models here.


class match(models.Model):
    team = models.TextField()
    venue = models.TextField()
    date = models.TextField()