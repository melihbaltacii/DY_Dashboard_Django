from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views





urlpatterns = [
    path('',LoginView.as_view(),name="home"),
    path('dashboard/',views.IndexView,name='dashboard'),

]
