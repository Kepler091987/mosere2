from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Jobs.forms import JobsForm
from Jobs.models import Jobs
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

@method_decorator(login_required, name='dispatch')
class JobsList(ListView):
    model = Jobs
    template_name = 'Jobs/jobs_list.html'

@method_decorator(login_required, name='dispatch')
class JobsCreate(CreateView):
    model = Jobs
    form_class = JobsForm
    template_name = 'Jobs/jobs_form_create.html'
    success_url = reverse_lazy('Jobs:jobs.index')

@method_decorator(login_required, name='dispatch')
class JobsUpdate(UpdateView):
    model = Jobs
    form_class = JobsForm
    template_name = 'Jobs/jobs_form_update.html'
    success_url = reverse_lazy('Jobs:jobs.index')

@method_decorator(login_required, name='dispatch')
class JobsDelete(DeleteView):
    model = Jobs
    form_class = JobsForm
    template_name = 'Jobs/jobs_delete.html'
    success_url = reverse_lazy('Jobs:jobs.index')


