from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    """Form for checking the validity of user data during registration"""

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):

    """Form for checking the validity of login data"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)