from django.contrib import admin

from app_main.models import User_app, Building, Token, Specialty, Group, Teacher, Classroom, Subject, Lesson, Section, \
    Change, Section, Receipt


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
    ordering = ('specialty', 'name')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('building', 'name')
    list_display_links = ('name',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    list_display_links = ('number',)
    ordering = ('number',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_subjects')

    def display_subjects(self, obj):
        return [Subject.name for Subject in obj.subject.all()]

    display_subjects.short_description = 'Предметы'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'start_time', 'duration', 'group', 'is_top', 'subject', 'teacher', 'classroom')
    list_display_links = ('start_time',)
    ordering = ('week_day', 'start_time', 'group')


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('date', 'lesson', 'subject', 'teacher', 'classroom')
    list_display_links = ('date',)
    ordering = ('date',)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('group', 'student', 'quantity', 'where', 'is_active')
    list_display_links = ('student',)
    ordering = ('is_active', 'group')
