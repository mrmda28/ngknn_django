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
