from django.urls import path
from bhojanapi import views

urlpatterns = [
    path('bhojan_api/',views.BhojanCRUDCBV.as_view()),
    ]