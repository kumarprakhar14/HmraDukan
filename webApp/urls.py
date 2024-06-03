from django.urls import path
from webApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    #path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]