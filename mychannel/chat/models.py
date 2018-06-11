from django.db import models

# Create your models here.

class Video(models.Model):
  url = models.URLField()
  vote = models.IntegerField(default=0)
  yt_id= models.CharField(max_length=100,unique=True)
  
  def __str__(self):
    return self.url
