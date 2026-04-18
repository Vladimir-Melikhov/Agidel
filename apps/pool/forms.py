from django import forms
from .models import Lead


class LeadForms(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone_number', 'use_messenger', 'messenger',
                  'whatsapp', 'telegram', 'max_m']

    def clean(self):
        cleaned_data = super().clean()
        use_messenger = cleaned_data.get('use_messenger')
        messenger = cleaned_data.get('messenger')
        whatsapp = cleaned_data.get('whatsapp')
        telegram = cleaned_data.get('telegram')
        max_m = cleaned_data.get('max_m')

        if use_messenger:
            if not messenger or messenger == 'none':
                self.add_error('messenger', "Выберите мессенджер из списка")
            elif messenger == 'whatsapp' and not whatsapp:
                self.add_error('whatsapp', "Укажите номер для WhatsApp")
            elif messenger == 'telegram' and not telegram:
                self.add_error('telegram', "Укажите никнейм в Telegram")
            elif messenger == 'max_m' and not max_m:  # ← исправлено
                self.add_error('max_m', "Заполните данные для этого мессенджера")

        return cleaned_data
