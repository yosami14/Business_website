from django.urls import path 
from .views import About_view,Home_view

urlpatterns = [
    path('about/', About_view , name = 'about_url'),
    path('', Home_view , name = 'home_url')
]
