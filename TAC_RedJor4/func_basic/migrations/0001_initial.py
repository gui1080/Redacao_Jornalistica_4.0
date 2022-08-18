# Generated by Django 4.0.6 on 2022-08-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Login',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
