from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('health/', views.HealthCheckView.as_view(), name='health'),
]
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('health/', views.HealthCheckView.as_view(), name='health'),
]