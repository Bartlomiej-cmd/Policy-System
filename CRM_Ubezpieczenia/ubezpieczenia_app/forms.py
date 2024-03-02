from django import forms
from .models import Client, Car, Policy, UserNotes, InsuranceAgency
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
        fields = ['client', 'car', 'number', 'value', 'date_end']


class AgencyForm(forms.ModelForm):
    class Meta:
        model = InsuranceAgency
        fields = ['name', 'address', 'contact_number', 'website']


class UserNotesForm(forms.ModelForm):
    class Meta:
        model = UserNotes
        fields = ['note', 'user', 'date']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()
        username = cd.get("username")
        password = cd.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError("Incorrect username or password")
        else:
            self.user = user
