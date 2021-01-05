from django.forms import ModelForm, TextInput, TimeField, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .views import *

from .models import *

# Comments
class CommentFrom(ModelForm):
    class Meta:
        model = Comment
        fields = ['creator', 'text']
        
class SupportFrom(ModelForm):
    class Meta:
        model = Support
        fields = ['text', 'user_support']
        