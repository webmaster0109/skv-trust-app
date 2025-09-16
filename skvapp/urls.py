from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<str:slug>/', views.skv_event_detail, name='skv_event_detail'),
    path('news/<str:slug>/', views.skv_news_detail, name='skv_news_detail'),
    path('about/', views.about, name='about'),
    path('shrikant-verma-trust-history/', views.skv_history, name='skv_history'),
]
