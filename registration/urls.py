from django.urls import path
from . import views # Make sure views are imported

urlpatterns = [
    
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    
    path('profile/', views.profile, name='profile'),
    
]