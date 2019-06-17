from django import forms
from django.forms import ModelForm
from .models import Comment
from django.db import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']

form = CommentForm
