from tkinter.tix import Form
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



class ModelInfoRetrieveRoomForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Rooms.objects.all(),)


class ModelsRetrieveForm(forms.Form):
    models = forms.ChoiceField(
        label='Раздел', required=True, choices=(
            ('room', 'Комната'),
            ('transfer', 'Трансфер'),
            ('tour', 'Тур'),
        ))


class ModelInfoRetrieveTourForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Tours.objects.all())


class ModelInfoRetrieveTransferForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Transfers.objects.all())


class ModelInfoRetrieveRoomOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Roomorders.objects.all())
    new_status = forms.ChoiceField(
        label='Status', required=True, choices=(
            ('New', 'New',), ('Conform', 'Conform'), ('Ready', 'Ready'),), )


class ModelInfoRetrieveTourOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Tourorders.objects.all())
    new_status = forms.ChoiceField(
        label='Status', required=True, choices=(
            ('New', 'New',), ('Conform', 'Conform'), ('Ready', 'Ready'),), )


class ModelInfoRetrieveTransferOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Transferorders.objects.all())
    new_status = forms.ChoiceField(label='Status', required=True, choices=(
        ('New', 'New',), ('Conform', 'Conform'), ('Ready', 'Ready'),), )


class ModelInfoRetrievePolicyRoomOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Roomorders.objects.all())
    policy = forms.CharField(label='Policy', required=True)


class ModelInfoRetrievePolicyTourOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Tourorders.objects.all())
    policy = forms.CharField(label='Policy', required=True)


class ModelInfoRetrievePolicyTransferOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Transferorders.objects.all())
    policy = forms.CharField(label='Policy', required=True)


class ModelInfoRetrievePriceRoomOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Roomorders.objects.all())
    price = forms.IntegerField(label='Цена', required=True)


class ModelInfoRetrievePriceTourOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Tourorders.objects.all())
    price = forms.IntegerField(label='Цена', required=True)


class ModelInfoRetrievePriceTransferOrderForm(forms.Form):
    id_s = forms.ModelChoiceField(
        label='ID', required=True, queryset=Transferorders.objects.all())
    price = forms.IntegerField(label='Цена', required=True)
