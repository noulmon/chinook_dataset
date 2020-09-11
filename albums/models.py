from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=120, blank=False)

    class Meta:
        db_table = 'artists'


class Album(models.Model):
    title = models.CharField(max_length=160, blank=False)
    artist = models.ForeignKey(Artist, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'albums'
