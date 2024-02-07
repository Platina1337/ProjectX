from django import forms
from django.contrib.auth import get_user_model
from .models import *

class AddPostModel(forms.ModelForm):
    class Meta:
        model = AppointMeeting
        fields = ['title', 'description', 'category']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['category'].queryset = Category.objects.all()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name','email','date','image','city'
        ]