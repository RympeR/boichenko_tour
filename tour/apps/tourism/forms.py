from django import forms
from .models import Users, Rooms, Tours, Transfers, Transferorders, Tourorders, Roomorders
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


class ModelInfoRetrieveRoomForm(AuthenticationForm):
    id_s = forms.ChoiceField(label='ID', required=True, choices=Rooms.objects.all().values_list('pk'),)


class ModelInfoRetrieveTourForm(AuthenticationForm):
    id_s = forms.ChoiceField(label='ID', required=True, choices=Tours.objects.all().values_list('pk'), )


class ModelInfoRetrieveTransferForm(AuthenticationForm):
    id_s = forms.ChoiceField(label='ID', required=True, choices=Transfers.objects.all().values_list('pk'), )


class ModelInfoRetrieveRoomOrderForm(AuthenticationForm):
    id_s = forms.ChoiceField(label='ID', required=True, choices=Roomorders.objects.all().values_list('pk'),)
    new_status = forms.ChoiceField(label='Status', required=True, choices=Roomorders.objects.all().values_list('pk'), )


class ModelInfoRetrieveTourOrderForm(AuthenticationForm):
    id_s = forms.ChoiceField(label='ID', required=True, choices=Tourorders.objects.all().values_list('pk'), )
    new_status = forms.ChoiceField(label='Status', required=True, choices=Tourorders.objects.all().values_list('pk'), )


class ModelInfoRetrieveTransferOrderForm(AuthenticationForm):
    id_s = forms.ChoiceField(label='ID', required=True, choices=Transferorders.objects.all().values_list('pk'), )
    new_status = forms.ChoiceField(label='Status', required=True, choices=Transferorders.objects.all().values_list('pk'), )
