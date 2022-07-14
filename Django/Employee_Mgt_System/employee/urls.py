from django.contrib import admin
from django.urls import path,include
from .import views 

urlpatterns = [
    path('',views.Index, name='home'),
    path('add',views.ADD, name='add'),
    path('edit',views.Edit,name='edit'),
    path('update/<str:id>',views.Update,name='update'),
    path('delete/<str:id>',views.Delete,name='delete'),
]
