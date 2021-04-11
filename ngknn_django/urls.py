from django.contrib import admin
from django.urls import path

from app_main.views import api_auth, api_users_app, api_specialty, api_group, api_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', api_auth),
    path('api/users_app/', api_users_app),
    path('api/specialties/', api_specialty),
    path('api/groups/', api_group),
    path('api/teachers/', api_teacher),
]
