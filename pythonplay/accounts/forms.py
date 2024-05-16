from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(
        max_length=150,
        required=False,
        label='',
        widget=forms.FileInput(attrs={
            'class': 'input_img'
        })
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Номер телефона'
        })
    )

    class Meta:
        model = Profile
        fields = ['image', 'phone']


class UserInfoForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия'
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Почта'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=128,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'old_password',
            'placeholder': 'Текущий пароль'
        })
    )
    new_password1 = forms.CharField(
        max_length=128,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Новый пароль'
        })
    )
    new_password2 = forms.CharField(
        max_length=128,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите пароль'
            })
    )
