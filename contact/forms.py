from .models import Contacs
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, EmailInput, URLInput


class ContacsForm(ModelForm):
    class Meta:
        model = Contacs
        fields = ['last_name', 'name', 'big_name', 'text', 'birth_day', 'num_ber', 'email', 'social']


        widgets = {

            "last_name": TextInput(attrs={
             'class': 'form-control',
             'placeholder': 'Фамилие'
            }),

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),

            "big_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),

            "text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите себя'
            }),

            "birth_day": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),

            "num_ber": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),

            "social": URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Соц. сеть'
            }),
        }