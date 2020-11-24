from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import RecordListItem


class RecordForm(ModelForm):
    class Meta:
        model = RecordListItem
        fields = '__all__'
