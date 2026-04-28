from django.core.mail import send_mail
from smtplib import SMTPException
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


def send_notification_email(instance, request=None):
    TIME = datetime.now().strftime('%d.%m.%Y %H:%M')

    messenger_row = ""
    if instance.use_messenger:
        messenger_row = f"""
        <tr>
            <td style="padding: 10px 0; border-bottom: 1px solid #4A90D9;">
                <span style="color: #AED6F1;">💬 Мессенджер</span>
            </td>
            <td style="padding: 10px 0; border-bottom: 1px solid #4A90D9; color: #ffffff; font-weight: bold;">
                {instance.messenger}
            </td>
        </tr>"""

    html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin: 0; padding: 0; background-color: #EAF4FB; font-family: Arial, sans-serif;">

        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td align="center" style="padding: 40px 20px;">

                    <table width="520" cellpadding="0" cellspacing="0"
                           style="background: linear-gradient(135deg, #1A6FA8, #2196C9);
                                  border-radius: 16px;
                                  overflow: hidden;
                                  box-shadow: 0 8px 32px rgba(26,111,168,0.25);">

                        <!-- Шапка -->
                        <tr>
                            <td colspan="2"
                                style="padding: 30px 30px 20px;
                                       border-bottom: 1px solid #4A90D9;
                                       text-align: center;">
                                <div style="font-size: 36px; margin-bottom: 8px;">🐥</div>
                                <div style="color: #ffffff; font-size: 22px; font-weight: bold;
                                            letter-spacing: 1px;">
                                    Новая заявка
                                </div>
                                <div style="color: #AED6F1; font-size: 13px; margin-top: 4px;">
                                    Агидель
                                </div>
                            </td>
                        </tr>

                        <!-- Тело -->
                        <tr>
                            <td colspan="2" style="padding: 20px 30px 30px;">
                                <table width="100%" cellpadding="0" cellspacing="0">

                                    <tr>
                                        <td style="padding: 10px 0; border-bottom: 1px solid #4A90D9;">
                                            <span style="color: #AED6F1;">👤 Имя</span>
                                        </td>
                                        <td style="padding: 10px 0; border-bottom: 1px solid #4A90D9;
                                                   color: #ffffff; font-weight: bold;">
                                            {instance.name}
                                        </td>
                                    </tr>

                                    <tr>
                                        <td style="padding: 10px 0; border-bottom: 1px solid #4A90D9;">
                                            <span style="color: #AED6F1;">📞 Телефон</span>
                                        </td>
                                        <td style="padding: 10px 0; border-bottom: 1px solid #4A90D9;
                                                   color: #ffffff; font-weight: bold;">
                                            {instance.phone_number}
                                        </td>
                                    </tr>

                                    {messenger_row}

                                    <tr>
                                        <td style="padding: 10px 0;">
                                            <span style="color: #AED6F1;">🕐 Время</span>
                                        </td>
                                        <td style="padding: 10px 0; color: #ffffff; font-weight: bold;">
                                            {TIME}
                                        </td>
                                    </tr>

                                </table>
                            </td>
                        </tr>

                        <!-- Подвал -->
                        <tr>
                            <td colspan="2"
                                style="padding: 16px 30px;
                                       background: rgba(0,0,0,0.15);
                                       text-align: center;
                                       color: #AED6F1;
                                       font-size: 12px;">
                                Это автоматическое уведомление — отвечать на него не нужно
                            </td>
                        </tr>

                    </table>
                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    try:
        send_mail(
            subject='🐥 Новая заявка — Агидель',
            message=f"Новая заявка от {instance.name}, телефон: {instance.phone_number}",
            from_email=EMAIL_HOST_USER,
            recipient_list=['b1esssed1@yandex.com', 'agidel_2018@mail.ru'],
            html_message=html,
        )
    except SMTPException as e:
        logger.error(f'Ошибка отправки на почту: {e}')
        raise