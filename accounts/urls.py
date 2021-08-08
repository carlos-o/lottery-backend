from django.urls import path
from accounts import views

urlpatterns = [
    path('signin/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]