from django.db import models

# Create your models here.

class Album(models.Model):
    types_of_albums = [
        ('EP', 'EP'),
        ('AL', 'ALBUM')
    ]
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    type = models.CharField(max_length=5, choices=types_of_albums, default='AL')
    songs = models.IntegerField()
    year_of_publish = models.IntegerField()
    image = models.ImageField(upload_to='media/static/images/',
                              null=True,
                              blank=True,
                              default="media/static/images/default.png")
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    track_number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name