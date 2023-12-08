from django import forms
from django.contrib.auth import get_user_model
from .models import *

class AddPostModel(forms.ModelForm):
    class Meta:
        model = AppointMeeting
        fields = '__all__'



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name','email','date','image','city'
        ]