from django.urls import path 
from .views import About_view,Home_view,Service_view,Team_view

urlpatterns = [
    path('', Home_view , name = 'home_url'),
    path('about/', About_view , name = 'about_url'),
    path('service/', Service_view , name = 'service_url'),
    path('team/', Team_view , name = 'team_url'),
]
