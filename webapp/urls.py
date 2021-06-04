from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='index'),
    path('user/<int:pk>/', views.details, name='detail'),
]