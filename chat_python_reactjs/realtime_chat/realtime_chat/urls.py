from django.urls import path
from chat import views

urlpatterns = [
    path('api/messages/', views.message_list, name='message_list'),
    path('create-group/', views.create_group),
    path('add-member/<str:group_id>/', views.add_member),
    path('send-message/<str:group_id>/', views.send_message),
]
