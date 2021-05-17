from django.urls import path
from . import views

urlpatterns = [
    path('api/devices/', views.api_devices, name='devices'),
    path('api/devices/<int:pk>/', views.api_device, name='device'),
    path('api/devices/<str:mac>/', views.api_device_mac, name='device_mac'),

    path('api/customers/', views.api_customers, name='customers'),
    path('api/customers/<int:pk>/', views.api_customer, name='customer'),

    path('api/extensions/', views.api_extensions, name='extensions'),
    path('api/extensions/<int:pk>/', views.api_extension, name='extension'),

    path('api/models/', views.api_models, name='models'),
    path('api/models/<int:pk>/', views.api_model, name='model'),

    path('api/vendors/', views.api_vendors, name='vendors'),
    path('api/vendors/<int:pk>/', views.api_vendor,name='vendors'),

    path('api/dsss/', views.api_dsss, name='dsss'),
    path('api/dsss/<int:pk>/', views.api_dss, name='dss'),

]
