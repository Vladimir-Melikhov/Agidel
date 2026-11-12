from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Lead
from .telegram import send_notification
from .email_notify import send_notification_email

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Lead)
def notifications(sender, instance, created, **kwargs):
    if not created:
        return

    request = getattr(instance, '_request', None)

    try:
        send_notification(instance, request)
    except Exception:
        logger.exception('Ошибка отправки Telegram-уведомления')

    try:
        send_notification_email(instance, request)
    except Exception:
        logger.exception('Ошибка отправки email-уведомления')