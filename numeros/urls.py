from django.urls import path
from . import views

urlpatterns = [
    path('extract/', views.extract_number, name='extract_number'),
    path('all-numbers/', views.show_all_numbers, name='show_all_numbers'),
]
