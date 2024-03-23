from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.input_sequence, name='input'),
    path('result/', views.result, name='result'),
    path('previous-results/', views.previous_results, name='previous_results'), 

]