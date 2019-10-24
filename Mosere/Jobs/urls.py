from django.urls import path
from .views import JobsUpdate, JobsCreate, JobsList, JobsDelete

urlpatterns = [
    path('', JobsList.as_view(), name='jobs.index'),
    path('create/', JobsCreate.as_view(), name='jobs.create'),
    path('edit/<int:pk>/', JobsUpdate.as_view(), name='jobs.update'),
    path('delete/<int:pk>/', JobsDelete.as_view(), name='jobs.delete'),
]