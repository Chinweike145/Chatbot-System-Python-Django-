from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),  # Root URL routed to chatbot view
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]