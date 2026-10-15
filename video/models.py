from django.db import models

class  video(models.Model):
    title = models.CharField(max_length=250, blank=True)
    video_size = models.CharField(max_length=250, blank=True)
    video_description = models.CharField()
    video_file = models.FileField()
    genre = models.CharField(max_length=200, blank=True)
    release_date= models.DateField()
    language = models.CharField(max_length=100, blank=True)
    age_rating = models.CharField(max_length=50, blank=True)
    cast = models.CharField()
    directors = models.CharField()
    produced_at = models.CharField(max_length=200, blank=True)
    thumbnail = models.ImageField()
    video_duration = models.DurationField()
