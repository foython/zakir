from django.db import models

# Create your models here.

class Staff(models.Model):
  POSITION_CHOICES = (
        ('1', 'Senior Faculty Member'),
        ('2', 'Faculty Member'),
  )

  name = models.CharField(max_length=32)
  position = models.CharField(choices=POSITION_CHOICES, max_length=32)
  facebook_link = models.URLField(max_length=64)
  twitter_link = models.URLField(max_length=64)
  linkedin_link = models.URLField(max_length=64)
  image = models.ImageField(upload_to = 'staff/')


  def __str__(self):
      return f'{self.name} {self.position}'