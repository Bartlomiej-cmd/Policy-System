from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.contrib.auth.models import User


# class Agent(models.Model):
#    login = models.CharField(max_length=128)
#    password = models.CharField(max_length=128)


class Agent(AbstractUser):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'agent'
        verbose_name_plural = 'agents'


Group.add_to_class('agent_group', models.ManyToManyField(Agent, related_name='group'))
Permission.add_to_class('agent_permission', models.ManyToManyField(Agent, related_name='user_permission'))

# Group.add_to_class('agent_group', models.ManyToManyField(Agent, related_name='agent_groups'))
# Permission.add_to_class('agent_permission', models.ManyToManyField(Agent, related_name='agent_user_permissions'))


# class AgentDatabaseEntry(models.Model):
#    agent = models.ForeignKey(User, on_delete=models.CASCADE)


class Car(models.Model):
    number = models.CharField(max_length=64)
    brand = models.CharField(max_length=128)
    year = models.IntegerField()
    vin = models.CharField(max_length=128)


class Client(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    pesel = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    agents = models.ManyToManyField(Agent)


class Policy(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    number = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    date_end = models.DateField()

