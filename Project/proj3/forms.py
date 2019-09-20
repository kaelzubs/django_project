from django import forms
from . models import Five_Page

class FiveForm(forms.ModelForm):
    class Meta:
        model = Five_Page
        fields = ['title', 'bodytext', 'created']