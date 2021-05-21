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
    is_admin = models.BooleanField('Администратор', default=False)

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
    image = models.ImageField('Изображение', upload_to='sections/', default='default.jpg', null=True, blank=True)
    url = models.URLField('URL')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Specialty(models.Model):
    name = models.CharField('Специальность', max_length=50)
    building = models.ForeignKey('Building', verbose_name='Корпус', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='specialties/', default='default.jpg', null=True, blank=True)

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


class Subject(models.Model):
    name = models.CharField('Название', max_length=70)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Teacher(models.Model):
    name = models.CharField('Преподаватель', max_length=70)
    email = models.EmailField('Email', default=None, null=True, blank=True)
    subject = models.ManyToManyField('Subject', verbose_name='Предметы', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Lesson(models.Model):
    week_day = models.IntegerField('День недели')
    start_time = models.TimeField('Начало занятия')
    duration = models.IntegerField('Продолжительность', default=90)
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


class Change(models.Model):
    date = models.DateField('Дата', default=(datetime.datetime.now() + datetime.timedelta(days=1)))
    lesson = models.ForeignKey('Lesson', verbose_name='Занятие', on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey('Subject', verbose_name='Предмет', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey('Teacher', verbose_name='Преподаватель', on_delete=models.CASCADE, null=True, blank=True)
    classroom = models.ForeignKey('Classroom', verbose_name='Кабинет', on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.TimeField('Начало занятия')
    duration = models.IntegerField('Продолжительность', default=90)

    def __str__(self):
        return str(str(self.pk))

    class Meta:
        verbose_name = 'Изменение'
        verbose_name_plural = 'Изменения'


class Receipt(models.Model):
    group = models.CharField('Группа', max_length=100)
    student = models.CharField('Студент', max_length=100)
    birthday = models.DateField('Дата рождения')
    quantity = models.IntegerField('Количество')
    where = models.CharField('Куда', max_length=150)
    military_commissariat = models.CharField('Военкомат', max_length=150, default=None, null=True, blank=True)
    is_active = models.BooleanField('Активные', default=True)

    def __str__(self):
        return str(self.group) + ', ' + str(self.student) + ', ' + str(self.quantity)

    class Meta:
        verbose_name = 'Справка'
        verbose_name_plural = 'Справки'
