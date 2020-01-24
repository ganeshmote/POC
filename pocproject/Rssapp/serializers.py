from rest_framework import serializers
from .models import *

class RssTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RssData
        fields = ['Title','Link','Publish_date','Description']

class RssTableSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Rssfeedclassified
        fields = '__all__'
