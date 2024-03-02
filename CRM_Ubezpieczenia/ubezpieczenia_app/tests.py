from audioop import reverse
import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import ClientForm, UserNotesForm, CarForm, PolicyForm
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


class TestClientModel(TestCase):

    def test_create_client(self, client):
        self.assertEqual(client.first_name, "Jan")
        self.assertEqual(client.last_name, "Kowalski")

    def test_can_create_client_with_user(self, user):
        client = Client.objects.create(
            user=user,
            first_name="Jan",
            last_name="Nowak",
            address="Wiejska 22",
            phone_number="500-500-500",
        )
        self.assertEqual(client.user, user)
        self.assertEqual(client.first_name, "Jan")


class TestViews(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_add_car_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('add_car'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_car.html')

    def test_add_policy_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('add_policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_policy.html')

    def test_add_client_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('add_client'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_client.html')

    def test_car_form(self):
        form_data = {'make': 'Toyota', 'model': 'Camry', 'year': '2022'}
        form = CarForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_policy_form(self):
        form_data = {'name': 'Policy 1', 'description': 'Test policy', 'premium': 100}
        form = PolicyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_client_form(self):
        form_data = {'name': 'Client 1', 'email': 'client@example.com', 'phone': '123456789'}
        form = ClientForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_client_notes_form(self):
        form_data = {'client': '1', 'note': 'Test note'}
        form = UserNotesForm(data=form_data)
        self.assertTrue(form.is_valid())


class CreateUserViewTests(TestCase):
    def test_create_user_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('create_user'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_create_user_failure(self):
        data = {
            'username': '',
            'password': ''
        }
        response = self.client.post(reverse('create_user'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='').exists())
