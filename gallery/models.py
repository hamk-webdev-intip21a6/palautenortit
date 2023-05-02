from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name="Kuva")
    description = models.CharField(max_length=200, verbose_name="Kuvateksti")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
