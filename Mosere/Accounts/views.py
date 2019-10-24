from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return reverse_lazy('Staff:staff.create', args=(self.object.id,))