from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=48)
    subtitle = models.CharField(max_length=64, default='')    
    content = models.TextField(verbose_name="Content", name='content', max_length=640*5)
    date = models.DateTimeField(verbose_name="Date", name='date')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title