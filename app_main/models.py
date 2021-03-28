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
    password = models.CharField('Пароль', max_length=50)
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
