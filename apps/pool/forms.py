from django import forms
from .models import Lead
import re


class LeadForms(forms.ModelForm):
    # Honeypot: скрытое поле, которое заполняют только боты
    website = forms.CharField(required=False)

    class Meta:
        model = Lead
        fields = [
            'name', 'phone_number', 'use_messenger', 'messenger',
            'consent_personal_data', 'consent_terms', 'consent_marketing',
        ]

    def clean_website(self):
        if self.cleaned_data.get('website'):
            raise forms.ValidationError('Спам')
        return ''

    def clean_phone_number(self):
        value = self.cleaned_data['phone_number'].strip()
        if not re.match(r'^[\d\+\(\)\ \-]+$', value):
            raise forms.ValidationError('Запрещенные символы')
        digits = re.sub(r'\D', '', value)
        if len(digits) < 11:
            raise forms.ValidationError('Введите номер полностью: +7 и 10 цифр')
        if len(digits) > 15:
            raise forms.ValidationError('Номер слишком длинный')
        return value

    def clean_consent_personal_data(self):
        if not self.cleaned_data.get('consent_personal_data'):
            raise forms.ValidationError('Необходимо согласие на обработку персональных данных')
        return True

    def clean_consent_terms(self):
        if not self.cleaned_data.get('consent_terms'):
            raise forms.ValidationError('Необходимо принять пользовательское соглашение')
        return True

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        use_messenger = cleaned_data.get('use_messenger')
        messenger = cleaned_data.get('messenger')

        if use_messenger and not messenger:
            self.add_error('messenger', 'Выберите мессенджер')
        if not use_messenger:
            cleaned_data['messenger'] = ''

        if name and any(char.isdigit() for char in name):
            self.add_error('name', 'В имени не может быть цифр')

        return cleaned_data
