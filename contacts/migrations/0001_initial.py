# Generated by Django 3.2.21 on 2023-09-25 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('dates', models.DateField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
