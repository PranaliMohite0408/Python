from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Index, name='home'),
    path('add', views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
]
