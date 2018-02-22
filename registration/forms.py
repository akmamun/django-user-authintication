from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",required=True)
    password = forms.CharField(label="Password", required=True,widget=forms.PasswordInput)

    def authenticate(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            return authenticate(username=username,password=password)