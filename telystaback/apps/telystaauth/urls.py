from django.urls import path

from . import views

app_name = 'telystaauth'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('refresh/', views.RefreshTokenView.as_view(), name='refresh'),
    path('activate/<str:token>/', views.ActivateUserView.as_view(), name='activate'),
]