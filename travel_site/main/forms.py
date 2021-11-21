from django import forms
from phonenumber_field.formfields import PhoneNumberField


class UserForm(forms.Form):
    """Форма обработки данных от пользователя"""

    username = forms.CharField(max_length=100, label="First name and Last name")
    phone_number = PhoneNumberField()
    email = forms.EmailField(max_length=50, label="Email")


class Subscribe_form(forms.Form):
    """Форма обработки данных от пользователя"""

    email = forms.EmailField(max_length=50, label="Email")
