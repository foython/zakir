from django.db import models

# Create your models here.
class Vision(models.Model):
  title = models.CharField(max_length=32)
  discription = models.CharField(max_length=512)
  image = models.ImageField(upload_to = 'vision/')

  def __str__(self):
      return f'{self.title}'