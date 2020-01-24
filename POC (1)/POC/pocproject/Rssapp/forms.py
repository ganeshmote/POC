from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from .models import Rss_Table


class UserForm(forms.ModelForm):

    class Meta:
        model = Rss_Table
        fields = ['Title', 'Link',
                  'Publish_date', 'Description']