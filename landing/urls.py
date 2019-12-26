from django.urls import path, include
from . import views
from rest_framework import routers
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('', include(router.urls)),
]
