from django.urls import path
from . import views

# TO SEND PATHS TO FUNCTIONS
urlpatterns = [
    path('', views.index, name="index"),
    path('employForm/', views.employForm, name="employForm"),
    path('employInfo/', views.employInfo, name="employInfo"),
]