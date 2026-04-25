from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from .telegram import send_notification
from .email_notify import send_notification_email
from django.contrib import messages


@receiver(post_save, sender=Lead)
def notifications(sender, instance, created, **kwargs):
    if created:
        request = getattr(instance, '_request', None)
        try:
            send_notification(instance, request)
            send_notification_email(instance, request)
        except Exception as e:
            if request:
                messages.error(request, 'Ошибка! Попробуйте позже')
