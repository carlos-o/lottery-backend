from django.urls import path
from lottery import views

urlpatterns = [
    path('participants/', views.ParticipantsView.as_view(), name='participants'),
    path('run/', views.LotteryRunView.as_view(), name='run'),
]