# Generated by Django 5.0.3 on 2024-03-25 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_credentials_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddresses',
            name='credentials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='credentials', to='core.credentials'),
        ),
    ]
