from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory_networks/', views.inventory_networks, name='inventory_networks'),
    path('device/<int:pk>', views.device, name='device'),
    path('discovery_networks/', views.networks, name='discovery_networks'),
    path('add_network/', views.add_network, name='add_network'),
    path('edit_network/<int:pk>', views.edit_network, name='edit_network'),
    path('delete_network/<int:pk>', views.delete_network, name='delete_network'),
    path('discovery_credentials/', views.credentials, name='discovery_credentials'),
    path('add_credentials/', views.add_credentials, name='add_credentials'),
    path('edit_credential/<int:pk>', views.edit_credential, name='edit_credential'),
    path('delete_credential/<int:pk>', views.delete_credential, name='delete_credential'),
    path('scan/<int:pk>', views.discover_scan, name='scan'),

]