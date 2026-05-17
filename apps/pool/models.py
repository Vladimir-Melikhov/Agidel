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
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('max_m', 'Max'),
    ]

    name = models.CharField("Имя", max_length=20)
    phone_number = models.CharField("Номер телефона", max_length=15)
    use_messenger =  models.BooleanField("сСвязаться в месенджере", default=False)
    messenger = models.CharField("Выбранный месенджер",max_length=10, choices=MESSENGER_CHOICES,
                                 default='none', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class Service(models.Model):
    title = models.CharField('Наименование', max_length=40)
    description = models.TextField('Описание', max_length=300)
    haveprice = models.BooleanField('Без Цены', default=False)
    price = models.PositiveIntegerField('Цена', blank=True, null=True)
    order_id = models.PositiveIntegerField('Порядок')
    is_active = models.BooleanField('Активно', default=False)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"
        ordering = ["order_id"]
    
    def __str__(self):
        return self.title

class Certificate(models.Model):
    img = models.ImageField('Изображение', upload_to='certificate/')
    title = models.CharField('Наименование', max_length=100, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['order']

    def __str__(self):
        return self.title or f'Сертификат #{self.pk}'
