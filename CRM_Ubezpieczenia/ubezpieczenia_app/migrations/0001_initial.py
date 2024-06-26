# Generated by Django 5.0.2 on 2024-02-27 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64)),
                ('brand', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('vin', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('pesel', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('agents', models.ManyToManyField(to='ubezpieczenia_app.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date_end', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubezpieczenia_app.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubezpieczenia_app.client')),
            ],
        ),
    ]
