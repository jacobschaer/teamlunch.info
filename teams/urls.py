from django.urls import path, include
from . import views

app_name = 'teams'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<slug:team_slug>/', views.view, name='view'),
    path('<slug:team_slug>/invite/', views.invite, name='invite'),
    path('<slug:team_slug>/lunches/', include('lunches.urls')),
]