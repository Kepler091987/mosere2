from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Staff.forms import StaffForm, UserStaffForm
from Staff.models import Staff
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.
@method_decorator(login_required, name='dispatch')
class StaffList(ListView):
    model = Staff
    template_name = 'Staff/staff_list.html'
    paginate_by = 2

@method_decorator(login_required, name='dispatch')
class StaffCreate(CreateView):
    model = Staff
    form_class = UserStaffForm
    template_name = 'Staff/staff_form_create.html'

    def form_valid(self, form):
        user = form['user'].save()
        staff = form['staff'].save(commit=False)
        staff.user = user
        staff.save()
        return HttpResponseRedirect(reverse('Staff:staff.index'))

@method_decorator(login_required, name='dispatch')
class StaffDetail(DetailView):
    model = Staff
    template_name = 'Staff/staff_detail.html'

@method_decorator(login_required, name='dispatch')
class StaffUpdate(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'Staff/staff_form_update.html'
    success_url = reverse_lazy('Staff:staff.index')

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(UpdateView, self).get_form_kwargs()
    #     kwargs.update({'pk': self.kwargs.get('pk')})
    #     return kwargs

@method_decorator(login_required, name='dispatch')
class StaffDelete(DeleteView):
    model = Staff
    form_class = StaffForm
    template_name = 'Staff/staff_delete.html'
    success_url = reverse_lazy('Staff:staff.index')
