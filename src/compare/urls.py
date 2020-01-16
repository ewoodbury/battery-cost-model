from django.urls import path

from . import views

urlpatterns = [
    path('', views.compare_view, name='compare_view'),
]