from django import forms
from .models import *

class AddPostModel(forms.ModelForm):
    class Meta:
        model = AppointMeeting
        fields = '__all__'