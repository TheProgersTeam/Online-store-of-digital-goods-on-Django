from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:pk>/', views.product, name='product'),
    path('faq/', views.faq, name='FAQ'),
    path('ban/', views.ban, name='BAN'),
]
