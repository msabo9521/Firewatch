# Generated by Django 5.0.3 on 2024-04-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_objectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectid',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='objectid',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]