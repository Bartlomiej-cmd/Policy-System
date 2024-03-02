# Generated by Django 5.0.2 on 2024-03-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubezpieczenia_app', '0003_usernotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurenceAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=64),
        ),
    ]
