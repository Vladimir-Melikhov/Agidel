
import os
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
URL_BOT = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'


def send_notification(instance, request=None):
    time = datetime.now().strftime('%d.%m.%Y %H:%M')

    text = (
        f"🔔 <b>Новая заявка</b>\n\n"
        f"👤 <b>Имя:</b> {instance.name}\n"
        f"📞 <b>Телефон:</b> {instance.phone_number}\n"
        f"🕐 <b>Время:</b> {time}"
    )

    if instance.use_messenger:
        text += f"\n💬 <b>Мессенджер:</b> {instance.messenger}"

    message = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(
            URL_BOT,
            json=message,
            timeout=(3, 5)
        )
        response.raise_for_status()

    except requests.exceptions.RequestException:
        logger.exception('Ошибка отправки в Telegram')
        raise
