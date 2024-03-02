from audioop import reverse
import pytest
from django.contrib.auth.models import User
from .forms import ClientForm, UserNotesForm, CarForm, PolicyForm
from .models import Client



@pytest.mark.django_db
class TestClientModel:
    def test_create_client(self, client):
        assert client.first_name == "Jan"
        assert client.last_name == "Kowalski"

    def test_can_create_client_with_user(self, user):
        client = Client.objects.create(
            user=user,
            first_name="Jan",
            last_name="Nowak",
            address="Wiejska 22",
            phone_number="500-500-500",
        )
        assert client.user == user
        assert client.first_name == "Jan"


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_add_car_view(self, client):
        client.login(username=self.username, password=self.password)
        response = client.get(reverse('add_car'))
        assert response.status_code == 200
        assert 'add_car.html' in [template.name for template in response.templates]

    def test_add_policy_view(self, client):
        client.login(username=self.username, password=self.password)
        response = client.get(reverse('add_policy'))
        assert response.status_code == 200
        assert 'add_policy.html' in [template.name for template in response.templates]

    def test_add_client_view(self, client):
        client.login(username=self.username, password=self.password)
        response = client.get(reverse('add_client'))
        assert response.status_code == 200
        assert 'add_client.html' in [template.name for template in response.templates]

    def test_car_form(self):
        form_data = {'make': 'Toyota', 'model': 'Camry', 'year': '2022'}
        form = CarForm(data=form_data)
        assert form.is_valid()

    def test_policy_form(self):
        form_data = {'name': 'Policy 1', 'description': 'Test policy', 'premium': 100}
        form = PolicyForm(data=form_data)
        assert form.is_valid()

    def test_client_form(self):
        form_data = {'name': 'Client 1', 'email': 'client@example.com', 'phone': '123456789'}
        form = ClientForm(data=form_data)
        assert form.is_valid()

    def test_client_notes_form(self):
        form_data = {'client': '1', 'note': 'Test note'}
        form = UserNotesForm(data=form_data)
        assert form.is_valid()


@pytest.mark.django_db
class TestCreateUserView:
    def test_create_user_success(self, client):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = client.post(reverse('create_user'), data)
        assert response.status_code == 302
        assert User.objects.filter(username='testuser').exists()

    def test_create_user_failure(self, client):
        data = {
            'username': '',
            'password': ''
        }
        response = client.post(reverse('create_user'), data)
        assert response.status_code == 200
        assert not User.objects.filter(username='').exists()