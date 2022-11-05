from django.db import models

# Create your models here.

class Artiste(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  Age = models.IntegerField(default=0)

 # def __str__(self):
  #  return self.firstname


class Song(models.Model):
  title = models.CharField(max_length=255)
  likes = models.IntegerField(default=0) ##number
  artiste_id = models.IntegerField(default=0)  ## integer
  date_released = models.DateField(auto_now=True)


class Lyric(models.Model):
  content = models.CharField(max_length=255)
  song_id = models.IntegerField(default=0)