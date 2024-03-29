from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50, unique=False)
    ip_address = models.GenericIPAddressField()
    type = models.CharField(max_length=50, unique=False)
    manufacturer = models.CharField(max_length=50, unique=False)
    device_model = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return f"{self.name}"

class Credentials(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, unique=False)
    community = models.CharField(max_length=50, unique=False, null=True, blank=True)
    username = models.CharField(max_length=50, unique=False, null=True, blank=True)
    password = models.CharField(max_length=50, unique=False, null=True, blank=True)
    enable = models.CharField(max_length=50, unique=False, null=True, blank=True)
    description = models.TextField(max_length=150, unique=False, null=True, blank=True)


    def __str__(self):
        return f"{self.name} {self.description}"

class Ipaddresses(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, unique=False)
    subnet = models.GenericIPAddressField(null=True, blank=True)
    host = models.GenericIPAddressField(null=True, blank=True)
    range = models.GenericIPAddressField(null=True, blank=True)
    frequency = models.CharField(max_length=50, unique=False, null=True)
    credentials = models.ForeignKey(Credentials, null=True, on_delete=models.SET_NULL, related_name='credentials')

    def __str__(self):
        return f"{self.name}"