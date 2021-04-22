from django.contrib import admin

from app_main.models import User_app, Building, Token, Specialty, Group, Teacher, Classroom, Subject, Lesson, Change


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


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('building', 'name')
    list_display_links = ('name',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_subjects')

    def display_subjects(self, obj):
        return ', '.join([Subject.name for Subject in obj.subject.all()])

    display_subjects.short_description = 'Предметы'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'start_time', 'duration', 'subject', 'group', 'teacher', 'classroom', 'is_top')
    list_display_links = ('start_time',)


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('date', 'lesson', 'teacher', 'subject', 'classroom', 'is_exists')
    list_display_links = ('date',)
