from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('facilities/', views.facilities, name='facilities'),
    path('patient-care/', views.patient_care, name='patient_care'),
    path('booking/', views.booking, name='booking'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('api/chat/', views.chat_api, name='chat_api'),
]
