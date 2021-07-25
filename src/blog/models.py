from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=80, blank=True)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.title
