from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    fio = forms.CharField(label='Имя', required=True, max_length=150, widget=forms.EmailInput(
        attrs={'required': True, 'placeholder': 'Имя:'}))
    username = forms.CharField(label='Имя', required=True, max_length=150, widget=forms.TextInput(
        attrs={'required': True, 'placeholder': 'Имя:'}))
    email = forms.EmailField(label='Почта', required=True, max_length=150, widget=forms.EmailInput(
        attrs={'required': True, 'placeholder': 'Логин:'}))
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(
        attrs={'required': True, 'placeholder': 'Пароль:', 'id': 'password'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True,  widget=forms.PasswordInput(
        attrs={'required': True, 'placeholder': 'Подтвердите пароль:', 'id': 'confirm_password'}))

    class Meta:
        model = Users
        fields = 'username', 'email', 'fio', 'password'

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # user.fio = self.cleaned_data['fio']

        if commit:
            user.save()

        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Логин', required=True, max_length=150, widget=forms.TextInput(
        attrs={'required': True, 'placeholder': 'Логин:'}))
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(
        attrs={'required': True, 'placeholder': 'Пароль:', 'id': 'password'}))
