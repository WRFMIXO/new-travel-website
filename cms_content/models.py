from django.db import models
from cms_users.models import AppUsers

# Create your models here.
class TextContent(models.Model):
    CONTENT_TYPES = [
        ('h1', 'Titre de niveau 1'),
        ('h2', 'Titre de niveau 2'),
        ('h3', 'Titre de niveau 3'),
        ('h4', 'Titre de niveau 4'),
        ('h5', 'Titre de niveau 5'),
        ('h6', 'Titre de niveau 6'),
        ('p1', 'Paragraphe de niveau 1'),
        ('p2', 'Paragraphe de niveau 2')
    ]
    content_model = models.CharField(max_length=5, choices=CONTENT_TYPES, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateField(blank=True, null=True)
    author = models.ForeignKey(AppUsers, models.DO_NOTHING, blank=True, null=True)

class MediaContent(models.Model):
    MEDIA_TYPES = [
        ('jpg', 'image JPEG'),
        ('png', 'Image PNG'),
        ('mp4', 'Vidéo MP4'),
        ('mp3', 'Audio MP3')
    ]
    media_model = models.CharField(max_length=5, choices=MEDIA_TYPES, blank=True, null=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')
    file_description = models.TextField()
    creation_date = models.DateField(blank=True, null=True)
    author = models.ForeignKey(AppUsers, models.DO_NOTHING, blank=True, null=True)