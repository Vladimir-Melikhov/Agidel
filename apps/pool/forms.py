from django import forms
from .models import Lead
import re


class LeadForms(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone_number', 'use_messenger', 'messenger',]

    def clean_phone_number(self):
        value = self.cleaned_data['phone_number']
        if not re.match(r'^[\d\+\(\)\ \-]+$', value):
            raise forms.ValidationError('Запрещенные символы')
        if len(value) < 10:
            raise forms.ValidationError('Номер слишком короткий')
        return value

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        phone_number = cleaned_data.get('phone_number')
        use_messenger = cleaned_data.get('use_messenger')
        messenger = cleaned_data.get('messenger')

        if use_messenger and not messenger:
            self.add_error('messenger', 'Выберие хотя бы один месенджер')

        if name and any(char.isdigit() for char in name):
            self.add_error('name', 'В имени не может быть цифр')

        return cleaned_data
