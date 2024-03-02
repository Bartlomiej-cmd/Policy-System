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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from ubezpieczenia_app import views
from ubezpieczenia_app.views import (
    CarListView,
    AddCarView,
    AddClientView,
    PolicyListView,
    ClientListView,
    AddPolicyView,
    UserListView,
    LoginView,
    LogoutView,
    UserNotesListView,
    AddUserNotesView,
    RegisterView,
    AddInsuranceAgencyView,
    AgencyListView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.database_view, name='database_view'),
    path('list_cars/', CarListView.as_view(), name='list_cars'),
    path('list_policies/', PolicyListView.as_view(), name='list_policies'),
    path('list_clients/', ClientListView.as_view(), name='list_clients'),
    path('list_usernotes/', UserNotesListView.as_view(), name='list_usernotes'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('add_client/', AddClientView.as_view(), name='add_client'),
    path('add_policy/', AddPolicyView.as_view(), name='add_policy'),
    path('add_usernotes/', AddUserNotesView.as_view(), name='add_usernotes'),
    path('list/users/', UserListView.as_view(), name="user-list"),
    path('add_agency/', AddInsuranceAgencyView.as_view(), name="add_agency"),
    path('list_agency/', AgencyListView.as_view(), name="list_agency"),
    path('create_user/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_list/', UserListView.as_view(), name="user_list"),
]


