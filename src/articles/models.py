from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)