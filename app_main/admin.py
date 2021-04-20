from django.contrib import admin

from app_main.models import User_app, Building, Token, Specialty, Group, Teacher, Type, Classroom, Subject, Lesson


@admin.register(User_app)
class UserAppAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'building')


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('number', 'address')
    ordering = ('number',)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('date', 'building', 'time', 'type', 'subject', 'group', 'teacher', 'classroom')
    list_display_links = ('date',)
