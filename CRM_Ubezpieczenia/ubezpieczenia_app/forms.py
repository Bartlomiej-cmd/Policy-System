from django import forms
from .models import Client, Car, Policy, Agent
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'pesel', 'phone', 'agents']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['number', 'brand', 'year', 'vin']


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['client', 'car', 'number', 'value', 'date_end',]


class AgentLoginForm(AuthenticationForm):
    class Meta:
        model = Agent
        fields = ['login', 'password']


class AgentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Agent
        fields = ['login']

