from django.contrib import admin
from django.urls import path,include
from . import views
# from .views import HomeView

urlpatterns = [
    path('',views.HomeView),
    path('calculate',views.CalculateView,name="calculate_fare")
]