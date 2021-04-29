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


class Section(models.Model):
    name = models.CharField('Секция', max_length=50)
    image = models.CharField('Путь к картинке', max_length=255)
    url = models.URLField('URL')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Specialty(models.Model):
    name = models.CharField('Специальность', max_length=50)
    building = models.ForeignKey('Building', verbose_name='Корпус', on_delete=models.CASCADE)
    image = models.CharField(verbose_name='Путь к картинке', max_length=255, null=True, blank=True)

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


class Classroom(models.Model):
    number = models.CharField('Номер', max_length=30)
    name = models.CharField('Название', max_length=70)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинет'


class Teacher(models.Model):
    name = models.CharField('Преподаватель', max_length=70)
    subject = models.ManyToManyField('Subject', verbose_name='Предметы', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Subject(models.Model):
    name = models.CharField('Название', max_length=70)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Lesson(models.Model):
    week_day = models.IntegerField('День недели')
    start_time = models.TimeField('Начало занятия')
    duration = models.IntegerField('Продолжительность')
    group = models.ForeignKey('Group', verbose_name='Группа', on_delete=models.CASCADE)
    is_top = models.BooleanField('Верхняя неделя', null=True, blank=True)
    subject = models.ForeignKey('Subject', verbose_name='Предмет', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', verbose_name='Преподаватель', on_delete=models.CASCADE)
    classroom = models.ForeignKey('Classroom', verbose_name='Кабинет', on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.pk))

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
