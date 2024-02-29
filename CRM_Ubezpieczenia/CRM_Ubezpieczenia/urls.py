"""
URL configuration for Ubezpieczenia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path
from ubezpieczenia_app import views
from ubezpieczenia_app.views import (
    # add_client,
    # add_car,
    # add_policy,
#   CarView,
#     agent_login,
#     agent_dashboard,
    database_view,
#   agent_database,
#     list_cars,
#     list_policies,
#     list_clients,
#    agent_signup,
    CarListView,
    AddCarView,
    AddClientView,
    PolicyListView,
    ClientListView,
    AddPolicyView,
    UserListView,
    LoginView,
    AddUserView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.database_view, name='database_view'),
#   path('add_client/', add_client, name='add_client'),
#   path('add_car/', add_car, name='add_car'),
#   path('add_policy/', add_policy, name='add_policy'),
#     path('agent_login/', agent_login, name='agent_login'),
#     path('agent_dashboard/', agent_dashboard, name='agent_dashboard'),
#   path('agent_database/', agent_database, name='agent_database'),
#   path('list_cars/', list_cars, name="list_cars"),
#   path('list_policies/', list_policies, name="list_policies"),
#   path('list_clients/', list_clients, name="list_clients"),
#   path('agent_signup/', agent_signup, name='agent_signup'),
    path('list_cars/', CarListView.as_view(), name='list_cars'),
    path('list_policies/', PolicyListView.as_view(), name='list_policies'),
    path('list_clients/', ClientListView.as_view(), name='list_clients'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('add_client/', AddClientView.as_view(), name='add_client'),
    path('add_policy/', AddPolicyView.as_view(), name='add_policy'),
    path('list/users/', UserListView.as_view(), name="user-list"),
    path('add_user/', AddUserView.as_view(), name="add_user"),
    path('login/', LoginView.as_view(), name="login"),
#   path('database_view/', database_view(), name='database_view'),
#   path('CarView/', CarView, name='cars_list')
]
