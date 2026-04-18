from django.db import models


class Actions(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    description = models.TextField("Описание", max_length=200)
    image = models.ImageField("Изображение", upload_to="promotions/", blank=True)
    is_active = models.BooleanField("Статус", default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.title


class Lead(models.Model):
    MESSENGER_CHOICES = [
        ('none', 'Не выбрано'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('max_m', 'Max'),
    ]

    name = models.CharField("Имя", max_length=20)
    phone_number = models.CharField("Номер телефона", max_length=15)
    use_messenger =  models.BooleanField("сСвязаться в месенджере", default=False)
    messenger = models.CharField("Выбранный месенджер",max_length=10, choices=MESSENGER_CHOICES,
                                 default='none', blank=True)
    whatsapp = models.CharField("Аккаунт ватсап", max_length=50, blank=True, null=True)
    telegram = models.CharField("Аккаунт телеграм", max_length=50, blank=True, null=True)
    max_m = models.CharField("Аккаунт макс", max_length=50, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'{self.name} - {self.phone_number}'
