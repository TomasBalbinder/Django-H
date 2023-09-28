from django import forms
from .models import Cosmonaut

class CosmonautForm(forms.ModelForm):
    class Meta:
        model = Cosmonaut
        fields = ['first_name', 'last_name']