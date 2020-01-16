from django.urls import path

from . import views

urlpatterns = [
    path('', views.cell_list, name='cell_list'),
    path('new/', views.new_cell, name='new_cell'),
]