from django.urls import path
from todoo import views

urlpatterns = [
    path('todoo/', views.todoo_list),
    path('todoo/<int:pk>/', views.todoo_detail),
]