from django.db import models

# Create your models here.


class Table(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название')
    count = models.IntegerField(verbose_name='Количество')
    distance = models.FloatField(verbose_name='Расстояние')
    date = models.TimeField(verbose_name='Дата')