from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    director = models.CharField(max_length=50, null=False)
    imdb_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title