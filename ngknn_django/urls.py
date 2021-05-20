from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from app_main.views import api_auth, api_users_app, api_specialty, api_group, api_teacher, api_classroom, \
    api_subject, api_lesson, api_lesson_t, api_change, api_change_t, api_lesson_with_change, api_lesson_with_change_t, \
    api_section, api_receipt, api_hash_password


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', api_auth),

    path('api/users_app/<int:pk>/', api_users_app),
    path('api/users_app/', api_users_app),

    path('api/specialties/<int:pk>/', api_specialty),
    path('api/specialties/', api_specialty),

    path('api/groups/<int:pk>/', api_group),
    path('api/groups/', api_group),

    path('api/teachers/<int:pk>/', api_teacher),
    path('api/teachers/', api_teacher),

    path('api/classrooms/<int:pk>/', api_classroom),
    path('api/classrooms/', api_classroom),

    path('api/subjects/<int:pk>/', api_subject),
    path('api/subjects/', api_subject),

    path('api/lessons/<int:pk_group>/<int:pk_week_day>/', api_lesson),
    path('api/lessons/<int:pk_group>/', api_lesson),
    path('api/lessons/', api_lesson),

    path('api/lessons_t/<int:pk_teacher>/<int:pk_week_day>/', api_lesson_t),
    path('api/lessons_t/<int:pk_teacher>/', api_lesson_t),
    path('api/lessons_t/', api_lesson_t),

    path('api/changes/<str:date>/', api_change),
    path('api/changes/', api_change),

    path('api/changes_t/<int:pk_teacher>/<str:date>/', api_change_t),
    path('api/changes_t/<int:pk_teacher>/', api_change_t),
    path('api/changes_t/', api_change_t),

    path('api/lessons_with_changes/<int:pk_group>/<str:date>/', api_lesson_with_change),
    path('api/lessons_with_changes/', api_lesson_with_change),

    path('api/lessons_with_changes_t/<int:pk_teacher>/<str:date>/', api_lesson_with_change_t),
    path('api/lessons_with_changes_t/<int:pk_teacher>/', api_lesson_with_change_t),
    path('api/lessons_with_changes_t/', api_lesson_with_change_t),

    path('api/sections/<int:pk>/', api_section),
    path('api/sections/', api_section),

    path('api/receipts/<int:pk>/', api_receipt),
    path('api/receipts/', api_receipt),

    path('api/hash_password/', api_hash_password),
]

urlpatterns += staticfiles_urlpatterns()
