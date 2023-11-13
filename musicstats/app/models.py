from django.db import models

# Create your models here.
class MISAMusic(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    job = models.CharField(max_length=125)
    work_unit = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    song_title = models.CharField(max_length=255)
    song_lyric = models.TextField()
    song_path = models.CharField(max_length=100, blank=True, null=True, default='')
    file_signature = models.FileField(upload_to='media', default='')

    def __str__(self) -> str:
        return self.song_title + " - " + self.full_name
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')


