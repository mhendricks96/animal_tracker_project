from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Animal
# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'

class AnimalListView(ListView):
  template_name = 'animal_list.html'
  model = Animal
  context_object_name = 'list_of_animals'

class AnimalDetailsView(DetailView):
  template_name = 'animal_details.html'
  model = Animal