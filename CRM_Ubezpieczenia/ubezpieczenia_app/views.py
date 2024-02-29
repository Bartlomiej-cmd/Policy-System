from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Client, Policy, Agent
from .forms import ClientForm, CarForm, PolicyForm, AgentLoginForm, AgentSignUpForm

@login_required
def database_view(request):
  cars = Car.objects.all()
  clients = Client.objects.all()
  policies = Policy.objects.all()
  return render(request, 'database_view.html', {'cars': cars, 'clients': clients, 'policies': policies})


def agent_login(request):
    if request.method == 'POST':
        form = AgentLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('database_view')
    else:
        form = AgentLoginForm()
    return render(request, 'agent_login.html', {'form': form})


def agent_signup(request):
    if request.method == 'POST':
        form = AgentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('agent_login')
    else:
        form = AgentSignUpForm()
    return render(request, 'agent_signup.html', {'form': form})


#@login_required
#def agent_database(request):
#    agent_data = AgentDatabaseEntry.objects.filter(agent=request.user)
#    return render(request, 'agent_database.html', {'agent_data': agent_data})


@login_required()
def agent_dashboard(request):
    clients = Client.objects.all()
    policies = Policy.objects.all()
    cars = Car.objects.all()
    return render(request, 'agent_dashboard.html', {'clients': clients, 'policies': policies, 'cars': cars})


@login_required
def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'list_cars.html', {'cars': cars})


@login_required
def list_policies(request):
    policies = Policy.objects.all()
    return render(request, 'list_policies.html', {'policies': policies})


@login_required
def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'list_clients.html', {'clients': clients})


@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database_view')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})


@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})


@login_required
def add_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('policy_list')
    else:
        form = PolicyForm()
    return render(request, 'add_policy.html', {'form': form})



