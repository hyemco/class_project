from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=20)
  description = models.TextField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)