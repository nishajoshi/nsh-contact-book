from django import forms
from django.core.validators import FileExtensionValidator


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    file = forms.FileField(
        label='Contacts File', required=True,
        validators=[FileExtensionValidator(allowed_extensions=['csv'])]
    )
