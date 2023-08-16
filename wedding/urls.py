from django.urls import path
from . import views

urlpatterns = [
    path('', views.weddingg, name='wedding'),
    path('wedding/<int:id>/', views.wedding_detail, name='wedding_detail'),
    path('search', views.search, name='search'),
    
]
