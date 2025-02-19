
from django.contrib import admin
from django.urls import path
from django.urls  import include


API_APPS = [
    ('auth','apps.telystaauth.urls'),
    ('home','apps.home.urls')
]
urlpatterns = [
    path('admin/', admin.site.urls),
]


for url_prefix, app_urls in API_APPS:
    urlpatterns.append(path(f'api/{url_prefix}/', include(app_urls)))