from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class RssDatas(models.Model):
    Title = models.CharField(max_length=400, null=False, blank=False)
    Link = models.CharField(max_length=400, null=False, blank=False)
    Publish_date = models.CharField(max_length=400, null=False, blank=False)
    Description = models.TextField()

    def __str__(self):
        return self.Title

class Rssfeedclassifieds(models.Model):
    Title = models.CharField(max_length=400, null=False, blank=False)
    Link = models.CharField(max_length=400, null=False, blank=False)
    Publish_date = models.CharField(max_length=400, null=False, blank=False)
    Description = models.TextField()
    classification = models.CharField(max_length=400, null=False, blank=False)
    insertDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Title

class RssData(models.Model):
    Title = models.CharField(max_length=400, null=False, blank=False)
    Link = models.CharField(max_length=400, null=False, blank=False)
    Publish_date = models.CharField(max_length=400, null=False, blank=False)
    Description = models.TextField()

    def __str__(self):
        return self.Title

class Rssfeedclassified(models.Model):
    Title = models.CharField(max_length=400, null=False, blank=False)
    Link = models.CharField(max_length=400, null=False, blank=False)
    Publish_date = models.CharField(max_length=400, null=False, blank=False)
    Description = models.TextField()
    classification = models.CharField(max_length=400, null=False, blank=False)
    insertDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Title

class Provided_RssLinks(models.Model):
    URL = models.CharField(max_length=400,null=False,blank=False,unique=True)
    Insert_Date = models.DateTimeField(auto_now_add=True)
    Process_N_Y = models.CharField(max_length=10,null=True)

class Provided_RssLink(models.Model):
    URL = models.CharField(max_length=400,null=False,blank=False,unique=True)
    Insert_Date = models.DateTimeField(auto_now_add=True)
    Process_N_Y = models.CharField(max_length=10,null=True)
