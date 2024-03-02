from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Car, Client, Policy, UserNotes, InsuranceAgency
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, get_user_model
from django.views.generic import (
    ListView,
    CreateView,
    FormView,
    RedirectView,
)
from .forms import (
    ClientForm,
    CarForm,
    PolicyForm,
    LoginForm,
    UserNotesForm,
    AgencyForm,
)

User = get_user_model()


def database_view(request):
    return render(request, 'database_view.html')


class UserListView(ListView):
    template_name = "user_list.html"
    model = User
    context_object_name = "users"


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("database_view")

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class RegisterView(FormView):
    template_name = 'create_user.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):

        form.save()

        return super().form_valid(form)


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'list_cars.html'
    context_object_name = 'cars'


class PolicyListView(LoginRequiredMixin, ListView):
    model = Policy
    template_name = 'list_policies.html'
    context_object_name = 'policies'


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'list_clients.html'
    context_object_name = 'clients'


class AddCarView(LoginRequiredMixin, CreateView):
    model = Car
    template_name = 'add_car.html'
    form_class = CarForm
    success_url = reverse_lazy('database_view')


class AddPolicyView(LoginRequiredMixin, CreateView):
    model = Policy
    template_name = 'add_policy.html'
    form_class = PolicyForm
    success_url = reverse_lazy('list_policies')


class AddClientView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('list_clients')


class UserNotesListView(LoginRequiredMixin, ListView):
    model = UserNotes
    template_name = 'list_usernotes.html'
    context_object_name = 'usernotes'


class AddUserNotesView(LoginRequiredMixin, CreateView):
    model = UserNotes
    template_name = 'add_usernotes.html'
    form_class = UserNotesForm
    success_url = reverse_lazy('list_usernotes')


class AgencyListView(ListView):
    model = InsuranceAgency
    template_name = 'list_agency.html'
    context_object_name = 'agencies'


class AddInsuranceAgencyView(CreateView):
    model = InsuranceAgency
    template_name = 'add_agency.html'
    form_class = AgencyForm
    success_url = reverse_lazy('list_agency')
