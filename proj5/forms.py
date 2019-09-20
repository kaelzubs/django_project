from django import forms
from . models import Disclaim_Page

class DisclaimForm(forms.ModelForm):
    class Meta:
        model = Disclaim_Page
        fields = ['title', 'bodytext', 'created']