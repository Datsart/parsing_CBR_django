from django.db import models


# Create your models here.

class CbrPars(models.Model):
    numcode = models.IntegerField(verbose_name='Код валюты')
    charcode = models.CharField(max_length=5, verbose_name='Сокращенный код валюты')
    nominal = models.IntegerField(verbose_name='Номинал')
    name = models.CharField(max_length=100, verbose_name='Название валюты')
    value = models.FloatField(verbose_name='Курс валюты')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering =['-value']

    def __str__(self):
        return self.name
