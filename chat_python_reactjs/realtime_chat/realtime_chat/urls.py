from django.urls import path
from chat import views

urlpatterns = [
    path('api/messages/', views.message_list, name='message_list'),
]
