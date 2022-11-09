

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_news.urls')),
    path('', include('app_parser.urls')),
    path('', include('app_registration.urls')),
    path('admin/', admin.site.urls),
]
