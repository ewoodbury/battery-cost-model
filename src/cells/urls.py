from django.urls import path

from . import views

urlpatterns = [

    path('', views.cell_list, name='cells_home'),
    path('cell_list', views.cell_list, name='cells_list'),

    path('new/', views.new_cell, name='new_cell'),

#     path('cell_input_confirm/', views.cell_input_confirm, name='cell_input_confirm'),

#     path('<int:cell_id>/', views.cell_detail, name='cell_detail'),

#     path('<int:cell_id>/edit', views.cell_edit, name='cell_edit'),

]