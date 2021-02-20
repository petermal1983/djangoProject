from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Введите адрес Вашей электронной почты', label="Адрес электронной почты")
    first_name = forms.CharField(max_length=100, help_text='Введите Ваше имя', label="Имя")
    last_name = forms.CharField(max_length=100, help_text='Введите Вашу фамилию', label="Фамилия")
    citizenship = forms.CharField(max_length=20, help_text='Введите Ваше гражданство', label="Гражданство")
    age = forms.IntegerField(help_text='Введите Ваш возраст', label="Возраст")
    adress = forms.CharField(widget=forms.Textarea,help_text='Введите Ваш адрес', label="Адрес")
    phone_num = forms.CharField(max_length=10, help_text='Введите телефон', label="Номер телефона")
    license_num = forms.CharField(max_length=25, help_text='Введите номер прав', label="Номер водительских прав")
    field_order = ["username", "password1", "password2", "email", "first_name", "last_name", "citizenship", "age", "adress", "phone_num", "licence_num"]


    class Meta:
        model = User
        fields = {'username',  'password1', 'password2', 'email', 'first_name', 'last_name', 'citizenship', 'age', 'adress', 'phone_num', 'license_num'}