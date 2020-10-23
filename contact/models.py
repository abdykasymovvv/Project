from django.db import models
from datetime import datetime


class Contacs(models.Model):
    """Контакты"""
    last_name = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=10)
    big_name = models.CharField('Отчество', max_length=20)
    text = models.TextField('Описание', max_length=100)
    birth_day = models.DateField('Дата рождение', default=datetime.today())
    num_ber = models.CharField('Номер', max_length=20)
    email = models.EmailField('Gmail', max_length=30)
    social = models.URLField('Соц сети', max_length=30)

    def __str__(self):
        return f'Контакты: {self.last_name} {self.name} {self.big_name} {self.text} {self.birth_day} {self.num_ber} {self.email} {self.social}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Люди'

