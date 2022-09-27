from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('',views.INDEX,name='home'),
    path('add',views.ADD, name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
