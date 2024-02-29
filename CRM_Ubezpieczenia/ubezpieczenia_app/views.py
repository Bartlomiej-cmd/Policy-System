from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Client, Policy
from .forms import ClientForm, CarForm, PolicyForm, LoginForm, AddUserForm
from django.views.generic import ListView, CreateView, FormView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


@login_required
def database_view(request):
    cars = Car.objects.all()
    clients = Client.objects.all()
    policies = Policy.objects.all()
    return render(request, 'database_view.html', {'cars': cars, 'clients': clients, 'policies': policies})


# def agent_login(request):
#     if request.method == 'POST':
#         form = AgentLoginForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('login')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('database_view')
#     else:
#         form = AgentLoginForm()
#     return render(request, 'agent_login.html', {'form': form})
#
#
# def agent_signup(request):
#     if request.method == 'POST':
#         form = AgentSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('agent_login')
#     else:
#         form = AgentSignUpForm()
#     return render(request, 'agent_signup.html', {'form': form})
#
#
# # @login_required
# # def agent_database(request):
# #     agent_data = AgentDatabaseEntry.objects.filter(agent=request.user)
# #     return render(request, 'agent_database.html', {'agent_data': agent_data})
#
#
# @login_required()
# def agent_dashboard(request):
#     clients = Client.objects.all()
#     policies = Policy.objects.all()
#     cars = Car.objects.all()
#     return render(request, 'agent_dashboard.html', {'clients': clients, 'policies': policies, 'cars': cars})

#----------------------------Tu jest nowy kod ------------------------------------------------------
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


class AddUserView(CreateView):
    template_name = "add_user.html"
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy("user-list")

# WIDOKI POLISY , KLIENTÓW I SAMOCHODÓW ####################################


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
    success_url = reverse_lazy('policy_list')


class AddClientView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


# @login_required
# def list_cars(request):
#     cars = Car.objects.all()
#     return render(request, 'list_cars.html', {'cars': cars})


# @login_required
# def list_policies(request):
#     policies = Policy.objects.all()
#     return render(request, 'list_policies.html', {'policies': policies})
#
#
# @login_required
# def list_clients(request):
#     clients = Client.objects.all()
#     return render(request, 'list_clients.html', {'clients': clients})
#
#
# @login_required
# def add_car(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('database_view')
#     else:
#         form = CarForm()
#     return render(request, 'add_car.html', {'form': form})
#
#
# @login_required
# def add_client(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('client_list')
#     else:
#         form = ClientForm()
#     return render(request, 'add_client.html', {'form': form})
#
#
# @login_required
# def add_policy(request):
#     if request.method == 'POST':
#         form = PolicyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('policy_list')
#     else:
#         form = PolicyForm()
#     return render(request, 'add_policy.html', {'form': form})
