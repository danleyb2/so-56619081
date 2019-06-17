from django.db import models

from datetime import datetime
from django import forms

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__ (self):
        return self.text
