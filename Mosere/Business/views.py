from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Business.forms import BusinessForm
from Business.models import Business
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class BusinessList(ListView):
    model = Business
    template_name = 'Business/business_list.html'

@method_decorator(login_required, name='dispatch')
class BusinessCreate(CreateView):
    model = Business
    form_class = BusinessForm
    template_name = 'Business/business_form_create.html'
    success_url = reverse_lazy('Business:business.index')

@method_decorator(login_required, name='dispatch')
class BusinessUpdate(UpdateView):
    model = Business
    form_class = BusinessForm
    template_name = 'Business/business_form_update.html'
    success_url = reverse_lazy('Business:business.index')

@method_decorator(login_required, name='dispatch')
class BusinessDelete(DeleteView):
    model = Business
    form_class = BusinessForm
    template_name = 'Business/business_delete.html'
    success_url = reverse_lazy('Business:business.index')
