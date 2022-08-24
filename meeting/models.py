from django.db import models

# Create your models here.


class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name

class Post(models.Model):
    fileName = models.CharField(max_length=200, null=True, default='')
    filePath = models.FileField(upload_to='Uploaded Files/', blank=True, null=True)
    uploadTime = models.DateField(auto_now = True)
    image = models.ImageField(upload_to = "images/", null=True, blank=True)

    def __str__(self):
        return str(self.fileName)
