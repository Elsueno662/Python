from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title