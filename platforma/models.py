from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    birth_date = models.DateField(auto_now=True, null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Kurs(models.Model):
    name  = models.CharField(max_length=100)
    price = models.IntegerField()
    start_date = models.DateField(auto_now=True, null=True, blank=True)
    end_date = models.DateField(auto_now=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Dars(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title



class Video(models.Model):
    dars = models.ForeignKey(Dars, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mp3', 'AVI', 'WMV', 'png', 'jpg',]) 
    ])
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dars.title


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.video.dars.title


class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    like = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.video.dars.title