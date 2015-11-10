from django.db import models
from django import forms
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=500, default="")
    subtitle = models.CharField(max_length=500, default="")
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')

class Article(Content):
    text = tinymce_models.HTMLField()

class Image(Content):
    path = models.FileField(upload_to=None,max_length=100)
    photographer = models.CharField(max_length=500, default="Unknown")

    def info(self):
    	return "The {0}, {1}, is by {2}".format(self.title,self.subtitle,self.contributors)


class Contributor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    content1 = models.ManyToManyField('Content',related_name='contributor',blank=True)

    def die(self):
    	self.delete(using=DEFAULT_DB_ALIAS)