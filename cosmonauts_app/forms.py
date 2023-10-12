from django import forms
from .models import Cosmonaut
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CosmonautForm(forms.ModelForm):
    class Meta:
        model = Cosmonaut
        fields = ['first_name', 'last_name']


class UploadFileForm(forms.Form):
    file = forms.FileField()


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Povinný. Zadejte platnou emailovou adresu.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



