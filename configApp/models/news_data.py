from django.db import models


class NewsFotos(models.Model):
    image = models.URLField()


class News(models.Model):
    title = models.CharField(max_length=255)
    images = models.ManyToManyField(NewsFotos, related_name="newsfotos")
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
