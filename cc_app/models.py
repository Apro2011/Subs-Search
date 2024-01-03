from django.db import models


# Create your models here.
class OutputLocationSetter(models.Model):
    location = models.CharField(max_length=100)


class VideoUpload(models.Model):
    video_file = models.FileField(upload_to="")
    # video_file_name = models.CharField(max_length=100)
