from django import  forms 
from django.forms import ModelForm

from .models import Contact
class contactbookForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
        'first_name',
        'last_name',
        'email',
        ]