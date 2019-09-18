from django import forms
from . models import About_Page

class AboutForm(forms.ModelForm):
    class Meta:
        model = About_Page
        fields = ['title', 'bodytext', 'created']