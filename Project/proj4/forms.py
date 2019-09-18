from django import forms
from . models import Ten_Page

class TenForm(forms.ModelForm):
    class Meta:
        model = Ten_Page
        fields = ['title', 'bodytext', 'created']