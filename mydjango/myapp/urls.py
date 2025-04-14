from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('service-choice/', views.service_choice_view, name='service_choice'),
    path('yanus-test/', views.yanus_test_view, name='yanus_test'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/api/', views.chat_api, name='chat_api'),
] 