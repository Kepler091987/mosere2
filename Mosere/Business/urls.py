from django.urls import path
from .views import BusinessList, BusinessCreate, BusinessUpdate, BusinessDelete

urlpatterns = [
    path('', BusinessList.as_view(), name='business.index'),
    path('create/', BusinessCreate.as_view(), name='business.create'),
    path('update/<int:pk>/', BusinessUpdate.as_view(), name='business.update'),
    path('delete/<int:pk>/', BusinessDelete.as_view(), name='business.delete'),
]