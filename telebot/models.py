from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length= 200, verbose_name='Token')
    tg_chat = models.CharField(max_length= 200, verbose_name='Chat_id')
    tg_text = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
