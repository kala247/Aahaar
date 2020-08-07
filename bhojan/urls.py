from django.urls import path
from bhojan import views

urlpatterns = [
    path('', views.home,name='home'),
    path('profile/', views.profile,name='profile'),
    path('wmenu/', views.weekmenu,name='wmenu'),
    path('menu/', views.partymenu,name='menu'),
    path('contact/', views.contactus,name='contact'),
    path('pmform/', views.partymenuadd,name='pmform'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('update/<int:id>/',views.updatemenu,name='update'),
    path('delete/<int:id>/',views.deleteitem,name='delete'),

    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout_view,name='logout'),

]