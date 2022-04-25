from django.db import models


class Rss(models.Model):
    title = models.CharField(max_length=255, null=True)
    url = models.URLField(null=True)


class News(models.Model):
    rss = models.ForeignKey(Rss, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)

