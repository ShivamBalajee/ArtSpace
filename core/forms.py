from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Username','class':'w-full py-4 px-4'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-4'}))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Username','class':'w-full py-4 px-4'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'w-full py-4 px-4'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-4'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Verify password', 'class': 'w-full py-4 px-4'}))