from django.urls import path
from .views import StaffList, StaffCreate, StaffDetail, StaffUpdate, StaffDelete

urlpatterns = [
    path('', StaffList.as_view(), name='staff.index'),
    path('create/', StaffCreate.as_view(), name='staff.create'),
    path('detail/<int:pk>/', StaffDetail.as_view(), name='staff.detail'),
    path('update/<int:pk>/', StaffUpdate.as_view(), name='staff.update'),
    path('delete/<int:pk>/', StaffDelete.as_view(), name='staff.delete'),
]