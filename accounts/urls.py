from django.urls import path
from accounts import views

urlpatterns = [
    path('signin/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('activate-account/', views.ActivateAccountView.as_view(), name="activate-account")
]