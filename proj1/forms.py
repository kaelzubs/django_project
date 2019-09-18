from django import forms
from . models import Home_Page

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home_Page
        fields = ['title', 'bodytext', 'created']
