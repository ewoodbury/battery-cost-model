from django.urls import path

from . import views

urlpatterns = [

    path('', views.price_list, name='price_list'),

    path('new/', views.new_price, name='new_price'),

#     path('cell_input_confirm/', views.cell_input_confirm, name='cell_input_confirm'),

#     path('<int:cell_id>/', views.cell_detail, name='cell_detail'),

#     path('<int:cell_id>/edit', views.cell_edit, name='cell_edit'),

]