from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('messages/', views.chat_messages, name='chat_messages'),
    path('settings/', views.system_settings, name='system_settings'),
    path('logs/', views.admin_logs, name='admin_logs'),
    path('messages/delete/<int:message_id>/', views.delete_message, name='delete_message'),
] 