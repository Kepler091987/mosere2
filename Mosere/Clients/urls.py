from django.urls import path
from .views import ClientsUpdate, ClientsCreate, ClientsDetail, ClientsList, ClientsDelete, DataFiscalCreate, CustomersAddressCreate, PhoneCreate, EmailCreate

urlpatterns = [
    path('', ClientsList.as_view(), name='clients.index'),
    path('create/', ClientsCreate.as_view(), name='clients.new'),
    path('detail/<int:pk>/', ClientsDetail.as_view(), name='clients.detail'),
    path('edit/<int:pk>/', ClientsUpdate.as_view(), name='clients.update'),
    path('delete/<int:pk>/', ClientsDelete.as_view(), name='clients.delete'),
    path('create/fiscal-data/<int:pk>/', DataFiscalCreate.as_view(), name='clients.create.datafiscal'),
    path('create/customer-address/<int:pk>/', CustomersAddressCreate.as_view(), name='clients.create.customeraddress'),
    path('create/phone/<int:pk>/', PhoneCreate.as_view(), name='clients.create.phone'),
    path('create/email/<int:pk>/', EmailCreate.as_view(), name='clients.create.email'),
]