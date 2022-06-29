from django import forms
from django.utils.text import slugify
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = (
            'name',
            'email',
            'message',
           
        )
