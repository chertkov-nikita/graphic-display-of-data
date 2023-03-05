from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=64)
    add_date = models.DateField()


class PageStats(models.Model):
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    date = models.DateTimeField()
    page_views = models.IntegerField()


class ContentStats(models.Model):
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=25)
    content_views = models.IntegerField()



