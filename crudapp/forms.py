from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Task


class TaskCreationForm(ModelForm):
    class Meta: 
        model = Task
        fields = '__all__'

