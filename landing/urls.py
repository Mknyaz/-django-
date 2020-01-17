from django.urls import path, include
from . import views
from rest_framework import routers
from masters import urls
router = routers.DefaultRouter()
router.register(r'subscriber', views.UserViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('master/<int:id>/', views.master, name='master'),
    path('master/<int:id>/landing', views.landing, name='landing'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('', include(router.urls)),
    path('master/<int:id>/landing/success/', views.success, name='success'),
    path('error/', views.error, name='error'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler404 = 'landing.views.handler404'
