from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from buyer.models import UserProfile, Products

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class UserCreationForm(forms.ModelForm):  
     class Meta:
        model = UserProfile
        fields = ["address", "mobile", "profile_pic" ]


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'category', 'photo', 'location')
        
                   
                   

        
