from django.db import models

# Create your models here.
class Home(models.Model):
  name = models.CharField(max_length=32)
  title = models.CharField(max_length=64)
  slogan = models.CharField(max_length=64)
  discription = models.CharField(max_length=512)
  image = models.ImageField(upload_to = 'home/')

  def __str__(self):
      return f'{self.name} {self.title}'


