from django import forms
from .models import Job
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['image','summary',]
        # fields = '__all__' # This is used when you want to capture all the fields
        labels = {
            'image':'Image',
            'summary':'Summary',
        }
# class PostUpdateForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.Textarea()