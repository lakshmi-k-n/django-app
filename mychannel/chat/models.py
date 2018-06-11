from django.db import models

# Create your models here.

class Votes(models.Model):
  url = models.URLField()
  vote = models.IntegerField(default=0)
  
  def __str__(self):
    return self.url
