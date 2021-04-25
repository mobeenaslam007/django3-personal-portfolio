from django.db import models
from datetime import date


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    description = models.TextField()

    def __str__(self):
        return self.title
    