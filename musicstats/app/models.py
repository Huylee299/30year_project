from django.db import models

# Create your models here.
class MISAMusic(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    job = models.CharField(max_length=125)
    work_unit = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    song_title = models.CharField(max_length=255)
    song_lyric = models.TextField()
    song_id = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.song_title + " - " + self.full_name

