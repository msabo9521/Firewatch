from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ip_address = models.GenericIPAddressField()
    type = models.CharField(max_length=50, unique=False, null=True, blank=True)
    manufacturer = models.CharField(max_length=50, unique=False, null=True, blank=True)
    device_model = models.CharField(max_length=50, unique=False, null=True, blank=True)
    serial = models.CharField(max_length=50, unique=False, null=True, blank=True)
    monitoring_interval = models.IntegerField(unique=False, null=True, blank=True)
    status = models.IntegerField(unique=False, null=True, blank=True)
    description = models.CharField(max_length=500, unique=False, null=True, blank=True)
    uptime = models.CharField(max_length=50, unique=False, null=True, blank=True)
    image =models.ImageField(upload_to='img/', unique=False, null=True, blank=True)

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
        return f"{self.name}"

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

class ObjectID(models.Model):
    oid = models.CharField(max_length=80, unique=True)
    vendor = models.CharField(max_length=50, unique=False)
    type = models.CharField(max_length=50, unique=False, null=True, blank=True)
    model = models.CharField(max_length=80, unique=False, null=True, blank=True)

    def __str__(self):
        return f"{self.oid} {self.vendor} {self.model}"

class Device_Stats(models.Model):
    device = models.ForeignKey(Device, null=True, on_delete=models.CASCADE, related_name='device')
    time = models.DateTimeField(auto_now_add=True)
    cpu = models.IntegerField(unique=False, null=True, blank=True)
    memory = models.IntegerField(unique=False, null=True, blank=True)
    disk = models.IntegerField(unique=False, null=True, blank=True)

    def __str__(self):
        return f"{self.time} {self.device}"