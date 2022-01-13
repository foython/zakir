from email.mime import image
from django.db import models

# Create your models here.
class Offer(models.Model):
  name = models.CharField(max_length=32)
  headline = models.CharField(max_length=128)
  image = models.ImageField(upload_to = 'offer/')

  def __str__(self):
      return f'{self.name}'