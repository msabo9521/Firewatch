from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import (
    AddCredentialsForm,
    AddIpaddressesForm,
)

from .models import (
    Ipaddresses,
    Credentials,
)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def networks(request):
    ipaddresses = Ipaddresses.objects.all()
    credentials = Credentials.objects.all()
    return render(request, 'networks.html', {'ipaddresses': ipaddresses, 'credentials':credentials})

def add_network(request):
    form = AddIpaddressesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('networks')

    return render(request, 'add_network.html', {'form': form})

def edit_network(request, pk):
    current_network = Ipaddresses.objects.get(id=pk)
    form = AddIpaddressesForm(instance=current_network)
    if request.method == "POST":
        form = AddIpaddressesForm(request.POST, instance=current_network)
        if form.is_valid():
            form.save()
            return redirect('networks')

    return render(request, 'edit_network.html', {'form': form, 'current_network':current_network})

def delete_network(request, pk):
    delete_net = Ipaddresses.objects.get(id=pk)
    delete_net.delete()
    messages.success(request, "Network Deleted")
    return redirect('networks')


def credentials(request):
    ipaddresses = Ipaddresses.objects.all()
    credentials = Credentials.objects.all()
    return render(request, 'credentials.html', {'ipaddresses': ipaddresses, 'credentials':credentials})

def add_credentials(request):
    form = AddCredentialsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_credentials = form.save()
            return redirect('credentials')

    return render(request, 'add_credentials.html', {'form': form})

def edit_credential(request, pk):
    current_credential = Credentials.objects.get(id=pk)
    form = AddCredentialsForm(instance=current_credential)
    if request.method == "POST":
        form = AddCredentialsForm(request.POST, instance=current_credential)
        if form.is_valid():
            form.save()
            return redirect('credentials')

    return render(request, 'edit_credential.html', {'form': form, 'current_credential':current_credential})

def delete_credential(request, pk):
    delete_cred = Credentials.objects.get(id=pk)
    delete_cred.delete()
    messages.success(request, "Credentials Deleted")
    return redirect('credentials')