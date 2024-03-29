from django import forms
from django.forms import Textarea, TextInput, PasswordInput, CharField, DateInput, ModelChoiceField

from .models import (
    Ipaddresses,
    Credentials
)

cred_types = (
    ("SNMPv1/2", "SNMPv1/2"),
    ("SSH", "SSH"),
    ("Windows", "Windows"),
)
ip_types = (
    ("subnet", "Subnet"),
    ("range", "Range"),
    ("host", "Host"),
)

class AddIpaddressesForm(forms.ModelForm):
    type = forms.ChoiceField(choices = ip_types, label="Type")
    subnet = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Subnet", "class":"form-control"}), label="Subnet")
    host = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Host", "class":"form-control"}), label="Host")
    range = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Range", "class":"form-control"}), label="Range")
    frequency = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Frequency", "class":"form-control"}), label="Frequency")
    credentials = ModelChoiceField(required=False, queryset=Credentials.objects.all(), widget=forms.Select(attrs={"placeholder":"Credentials",'class': 'form-control'}))

    class Meta:
        model = Ipaddresses
        exclude = ("user",)

class AddCredentialsForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control", 'required': 'True'}), label="Name")
    type = forms.ChoiceField(choices = cred_types, label="Type")
    community = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Community", "class":"form-control"}), label="Community")
    username = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Username", "class":"form-control"}), label="Username")
    password = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Password", "class":"form-control"}), label="Password")
    enable = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Enable", "class":"form-control"}), label="Enable")
    description = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), label="Description")

    class Meta:
        model = Credentials
        exclude = ("user",)
