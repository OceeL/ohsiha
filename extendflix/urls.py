
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('data_page', views.data_page, name='data_page'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view()),

]