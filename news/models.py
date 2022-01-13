from django.db import models

# Create your models here.
class News(models.Model):
  title = models.CharField(max_length=32)
  publish_date = models.DateTimeField(auto_now=True)
  discription = models.CharField(max_length=1024)
  image = models.ImageField(upload_to = 'news/')

  def __str__(self):
      return f'{self.title}'