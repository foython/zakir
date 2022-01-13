from django.db import models

# Create your models here.
class Mission(models.Model):
  name = models.CharField(max_length=32)
  discription = models.CharField(max_length=512)
  image = models.ImageField(upload_to = 'mission/')

  def __str__(self):
      return f'{self.name}'