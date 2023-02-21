from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class imageUpload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=1000,blank=False,null=False)
    genre = models.ForeignKey('Genre',on_delete=models.SET_NULL,blank=False,null=True)
    image = models.ImageField(blank=False,null=False,upload_to='images/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title