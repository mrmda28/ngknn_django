from django.contrib import admin
from django.urls import path

from app_main.views import api_auth, api_create_user_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', api_auth),
   path('api/create_user_app/', api_create_user_app),
]
