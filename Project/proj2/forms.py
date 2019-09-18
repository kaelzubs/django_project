from django import forms
from . models import Three_Page

class ThreeForm(forms.ModelForm):
    class Meta:
        model = Three_Page
        fields = ['title', 'bodytext', 'created']