from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, unique=True, verbose_name="URL (auto generated. Don't touch)")
    img = models.ImageField(upload_to='pics')
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    uploader = models.TextField(max_length=30)
    

    def __str__(self):
        return self.name