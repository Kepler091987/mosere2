from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Clients.forms import ClientsForm, CustomersAddressForm, FiscalDataForm, PhonesForm, EmailsForm, \
    ClientPhoneEmailCustomersAddressForm
from Clients.models import Clients, customersAddress, fiscalData, Phones, Emails
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ClientsList(ListView):
    model = Clients
    template_name = 'Clients/clients_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['addresses'] = customersAddress.objects.all()
        context['phones'] = Phones
        return context




@method_decorator(login_required, name='dispatch')
class ClientsCreate(CreateView):
    model = Clients
    form_class = ClientPhoneEmailCustomersAddressForm
    template_name = 'Clients/clients_form_create.html'

    def form_valid(self, form):
        client = form['client'].save()
        phone = form['phone'].save(commit=False)
        phone.client = client
        phone.save()
        email = form['email'].save(commit=False)
        email.client = client
        email.save()
        customersAddress = form['customersAddress'].save(commit=False)
        customersAddress.client = client
        customersAddress.save()
        return HttpResponseRedirect(reverse('Clients:clients.index'))
        # return reverse_lazy('Clients:clients.index')



@method_decorator(login_required, name='dispatch')
class ClientsDetail(DetailView):
    model = Clients
    template_name = 'Clients/clients_detail.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(DetailView, self).get_context_data(**kwargs)
        context['client'] = Clients.objects.get(pk=pk)
        context['customersAddress'] = customersAddress.objects.filter(client=pk)
        context['datafiscal'] = fiscalData.objects.filter(client=pk)
        context['phones'] = Phones.objects.filter(client=pk)
        context['emails'] = Emails.objects.filter(client=pk)
        return context

@method_decorator(login_required, name='dispatch')
class ClientsUpdate(UpdateView):
    model = Clients
    form_class = ClientsForm
    template_name = 'Clients/clients_form_update.html'
    success_url = reverse_lazy('Clients:clients.index')

@method_decorator(login_required, name='dispatch')
class ClientsDelete(DeleteView):
    model = Clients
    form_class = ClientsForm
    template_name = 'Clients/clients_delete.html'
    success_url = reverse_lazy('Clients:clients.index')

@method_decorator(login_required, name='dispatch')
class DataFiscalCreate(CreateView):
    model = fiscalData
    form_class = FiscalDataForm
    template_name = 'Clients/data_fiscal_form.html'
    success_url = reverse_lazy('Clients:clients.index')


@method_decorator(login_required, name='dispatch')
class CustomersAddressCreate(CreateView):
    model = customersAddress
    form_class = CustomersAddressForm
    template_name = 'Clients/customers_address_form.html'
    success_url = reverse_lazy('Clients:clients.index')

@method_decorator(login_required, name='dispatch')
class PhoneCreate(CreateView):
    model = Phones
    form_class = PhonesForm
    template_name = 'Clients/phone_form.html'
    success_url = reverse_lazy('Clients:clients.index')


@method_decorator(login_required, name='dispatch')
class EmailCreate(CreateView):
    model = Emails
    form_class = EmailsForm
    template_name = 'Clients/email_form.html'
    success_url = reverse_lazy('Clients:clients.index')



