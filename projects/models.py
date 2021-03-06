from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="projects/images")
    url = models.URLField(blank=True)  # blank=True means optional
    
    def __str__(self):
        return self.title 
    