from django import forms
from . models import Contact_Page

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Page
        fields = ['title', 'bodytext', 'created']


class ContactForms(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)