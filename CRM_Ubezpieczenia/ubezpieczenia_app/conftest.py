import pytest
from django.contrib.auth.models import User
from .models import Client


@pytest.fixture
def user(django_db_setup):
    user = User.objects.create_user(username="test_user", password="test_password")
    return user


@pytest.fixture
def client(django_db_setup):
    client = Client.objects.create(
        first_name="Jan", last_name="Kowalski", address="Wiejska 22", phone_number="500-500-500"
    )
    return client