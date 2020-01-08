from django.urls import path

from . import views

urlpatterns = [

    path('', views.run_model, name='run_model'),

    path('confirm', views.run_model_confirm, name='run_model_confirm'),

    path('<int:model_id_input>/', views.view_model, name='view_model'),

    # path('new/', views.new_cell, name='new_cell'),

#     path('cell_input_confirm/', views.cell_input_confirm, name='cell_input_confirm'),

#     path('<int:cell_id>/', views.cell_detail, name='cell_detail'),

#     path('<int:cell_id>/edit', views.cell_edit, name='cell_edit'),

]