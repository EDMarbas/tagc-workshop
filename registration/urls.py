from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    
    path('profile/', views.profile, name='profile'),

    path('faq/', TemplateView.as_view(template_name='registration/faq.html'), name='faq'),
    
]