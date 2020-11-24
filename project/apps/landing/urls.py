from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.LandingHome.as_view(), name = 'home')
]
