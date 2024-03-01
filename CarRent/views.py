from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from CarRent.models import Car
from CarRent.forms import CarForm


class CarListView(ListView):
    template_name = 'index.html'
    model = Car
    queryset = Car.objects.all()
    context_object_name = 'cars_list'

class CarRentDetailView(DetailView):
    template_name = 'car_detail.html'
    model = Car
    context_object_name = 'car_detail'

class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'car_create.html'
    success_url = '/CarRent/'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    context_object_name = 'CarRent'
    success_url = '/CarRent/'

class CarDeleteView(DeleteView):
    template_name = 'car_confirm_delete.html'
    context_object_name = 'CarRent'
    model = Car
    success_url = '/CarRent/'
    

