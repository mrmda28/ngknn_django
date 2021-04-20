from django.contrib import admin
from django.urls import path

from app_main.views import api_auth, api_users_app, api_specialty, api_group, api_teacher, api_type, api_classroom, \
    api_subject, api_lesson

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', api_auth),

    path('api/users_app/', api_users_app),
    path('api/users_app/<int:pk>/', api_users_app),

    path('api/specialties/', api_specialty),
    path('api/specialties/<int:pk>/', api_specialty),

    path('api/groups/', api_group),
    path('api/groups/<int:pk>/', api_group),

    path('api/teachers/', api_teacher),
    path('api/teachers/<int:pk>/', api_teacher),

    path('api/types/', api_type),
    path('api/types/<int:pk>/', api_type),

    path('api/classrooms/', api_classroom),
    path('api/classrooms/<int:pk>/', api_classroom),

    path('api/subjects/', api_subject),
    path('api/subjects/<int:pk>/', api_subject),

    path('api/lessons/', api_lesson),
    path('api/lessons/<int:pk>/', api_lesson),
]
