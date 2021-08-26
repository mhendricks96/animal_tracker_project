from django.urls import path
from django.urls.resolvers import URLPattern
from .views import AnimalListView, HomeView, AnimalDetailsView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('animal_list/', AnimalListView.as_view(), name='animal_list'),
  path('<int:pk>', AnimalDetailsView.as_view(), name='animal_details')
]