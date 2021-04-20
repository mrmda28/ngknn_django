import datetime
from django.db import models


class Building(models.Model):
    number = models.IntegerField('Корпус')
    address = models.CharField('Адрес', max_length=80)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы'


class User_app(models.Model):
    username = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=10)
    password = models.CharField('Пароль', max_length=128)
    building = models.ForeignKey('Building', verbose_name='Корпус', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Token(models.Model):
    token = models.CharField('Токен', max_length=50)
    user = models.ForeignKey('User_app', verbose_name='Пользователь', on_delete=models.CASCADE)
    date_created = models.DateField('Дата создания', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'


class Specialty(models.Model):
    name = models.CharField('Специальность', max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Group(models.Model):
    name = models.CharField('Группа', max_length=10)
    specialty = models.ForeignKey('Specialty', verbose_name='Специальность', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Teacher(models.Model):
    name = models.CharField('Преподаватель', max_length=70)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Type(models.Model):
    name = models.CharField('Тип', max_length=70)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Classroom(models.Model):
    number = models.IntegerField('Номер')
    name = models.CharField('Название', max_length=70)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинет'


class Subject(models.Model):
    name = models.CharField('Название', max_length=70)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Lesson(models.Model):
    date = models.DateField('Дата', default=(datetime.datetime.now() + datetime.timedelta(days=1)))
    building = models.ForeignKey('Building', verbose_name='Корпус', on_delete=models.CASCADE)
    time = models.TimeField('Время')
    duration = models.IntegerField('Продолжительность')
    type = models.ForeignKey('Type', verbose_name='Тип', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', verbose_name='Предмет', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', verbose_name='Группа', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', verbose_name='Преподаватель', on_delete=models.CASCADE)
    classroom = models.ForeignKey('Classroom', verbose_name='Кабинет', on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.date) + str(self.time))

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
