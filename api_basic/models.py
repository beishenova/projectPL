from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="pictures/", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
