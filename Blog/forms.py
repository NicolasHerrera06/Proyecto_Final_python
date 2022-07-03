from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contacto, Posteo

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contrasena' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        help_texts = {k:"" for k in fields} 

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre","correo","tipo_consulta","mensaje"]
        fields = '__all__'

class PostForm(forms.ModelForm):

    class Meta:
        model = Posteo
        #fields = ["nombre","correo","tipo_consulta","mensaje"]
        fields = '__all__'