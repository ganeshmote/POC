from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models


# class RssData(models.Model):
#
#     Title = models.CharField(max_length=50, null=False, blank=False)
#     Link = models.CharField(max_length=30, null=False, blank=False)
#     Publish_date = models.CharField(max_length=30, null=False, blank=False)
#     Description = models.TextField(null=False, blank=False)
#     insert_date = models.DateTimeField(null=True)
#     classification = models.CharField(max_length=300,null=True)
#     invester = models.CharField(max_length=50,null=True)
#     investing_In = models.CharField(max_length=50,null=True)
#     acquire_By = models.CharField(max_length=50,null=True)
#     merging_In = models.CharField(max_length=50,null=True)

class Rss_Table(models.Model):
    Title = models.CharField(max_length=255, null=False, blank=False)
    Link = models.CharField(max_length=255, null=False, blank=False)
    Publish_date = models.CharField(max_length=225, null=False, blank=False)
    Description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.Title



class Rssfeedclassified(models.Model):

    Title = models.CharField(max_length=300, null=False, blank=False)
    Link = models.CharField(max_length=300, null=False, blank=False)
    Publish_date = models.CharField(max_length=300, null=False, blank=False)
    Description = models.TextField()
    classification = models.CharField(max_length=300, null=False, blank=False)
    insertDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Title


class RssData(models.Model):

    Title = models.CharField(max_length=300, null=False, blank=False)
    Link = models.CharField(max_length=300, null=False, blank=False)
    Publish_date = models.CharField(max_length=300, null=False, blank=False)
    Description = models.TextField()

    def __str__(self):
        return self.Title