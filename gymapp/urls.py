from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('trainer/', views.trainer, name='trainer'),
    path('courses/', views.courses, name='course'),
    path('service/', views.service, name='service'),
]
