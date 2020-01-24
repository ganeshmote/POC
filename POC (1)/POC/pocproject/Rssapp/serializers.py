from rest_framework import serializers
from .models import *


class RssTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rss_Table
        fields = ['Title',
                  'Link',
                  'Publish_date',
                  'Description']


class rssClassifySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Rssfeedclassified
        fields = ['Title',
                  'Link',
                  'Publish_date',
                  'Descripton',
                  'classification',
                  'insertDate']
