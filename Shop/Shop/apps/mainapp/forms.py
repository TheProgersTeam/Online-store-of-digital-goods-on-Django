from django.forms import ModelForm
from .views import *
from .models import *


# Comments
class CommentFrom(ModelForm):
    class Meta:
        model = Comment
        fields = ['creator', 'text']


# Support
class SupportFrom(ModelForm):
    class Meta:
        model = Support
        fields = ['text', 'user_support']
