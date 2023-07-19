from django.db import models

# Create your models here.
class boardList(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    content =models.TextField()
    
    time = models.DateTimeField(auto_now=True)
    

class commentList(models.Model):
    
    comment =models.TextField()
    
class userList(models.Model):
    name = models.CharField(max_length=4)
    
    password =models.CharField(max_length=20)