from django import forms
from .models import Client, Car, Policy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'pesel', 'phone', 'users']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['number', 'brand', 'year', 'vin']


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['client', 'car', 'number', 'value', 'date_end',]


# class AgentLoginForm(AuthenticationForm):
#     class Meta:
#         model = Agent
#         fields = ['login', 'password']
#
#
# class AgentSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Agent
#         fields = ['login']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()
        username = cd.get("username")
        password = cd.get("password")
        user = authenticate(username=username,password=password)

        if user is None:
            raise ValidationError("Incorrect username or password")
        else:
            self.user = user


class AddUserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']
        widgets = {
            "password": forms.PasswordInput,
            "email": forms.EmailInput,
        }

    def clean(self):
        cd = super().clean()
        pass1 = cd.get('password')
        pass2 = cd.get('password2')

        if pass1 != pass2:
            raise ValidationError('Hasła nie są identyczne.')