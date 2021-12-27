from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'select']


class StuffForm(ModelForm):
    class Meta:
        model = Stuff
        fields = ['fullname', 'age', 'position', 'image']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'text', 'price', 'image', 'filter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}),
            'filter': forms.Select(attrs={'class': 'form-control'}),
        }


class ProductupdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'text', 'price', 'image', 'filter']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']