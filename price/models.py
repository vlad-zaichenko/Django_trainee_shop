from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=200, verbose_name='Цена')
    pc_descritpion = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'



class PriceTable(models.Model):
    pt_description = models.CharField(max_length=200, verbose_name='Услуга')
    pt_old = models.CharField(max_length=200, verbose_name='Старая цена')
    pt_new = models.CharField(max_length=200, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_description

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
