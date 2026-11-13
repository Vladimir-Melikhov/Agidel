import os
import threading
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
# Необязательно: прокси, если с сервера нет доступа к api.telegram.org.
# Примеры: http://user:pass@host:port, socks5h://user:pass@host:port
TELEGRAM_PROXY = os.getenv('TELEGRAM_PROXY', '').strip()
URL_BOT = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
ADMIN_URL = 'https://agidelreutov.ru/admin/pool/lead/'


def _post(message):
    proxies = {'http': TELEGRAM_PROXY, 'https': TELEGRAM_PROXY} if TELEGRAM_PROXY else None
    try:
        response = requests.post(
            URL_BOT,
            json=message,
            timeout=(5, 10),
            proxies=proxies,
        )
        response.raise_for_status()
    except requests.exceptions.RequestException:
        # Не логируем URL с токеном: исключение requests содержит его в тексте.
        logger.error('Ошибка отправки в Telegram (прокси: %s)', 'да' if proxies else 'нет', exc_info=False)
        raise


def send_notification(instance, request=None):
    """Уведомление без персональных данных: Telegram — зарубежный сервис."""
    time = datetime.now().strftime('%d.%m.%Y %H:%M')

    text = (
        f"🔔 <b>Новая заявка</b>\n\n"
        f"🕐 {time}\n"
        f"Данные — в <a href=\"{ADMIN_URL}\">админ-панели</a>"
    )

    message = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }

    # В фоне, чтобы недоступность Telegram не тормозила отправку формы.
    def runner():
        try:
            _post(message)
        except Exception:
            pass

    threading.Thread(target=runner, daemon=True).start()
