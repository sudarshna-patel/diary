from django.urls import path
from .views import index, add

# app_name = 'entries'
urlpatterns = [
    path('', index, name='home'),
    path('add/', add, name='add'),
]