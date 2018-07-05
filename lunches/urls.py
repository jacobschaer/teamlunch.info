from django.urls import path

from . import views

app_name = 'lunches'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('location_search/', views.location_search, name='location_search'),
]