# Generated by Django 5.0.3 on 2024-03-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_address', models.GenericIPAddressField()),
                ('type', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('device_model', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_address', models.GenericIPAddressField()),
                ('type', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('device_model', models.CharField(max_length=50)),
            ],
        ),
    ]