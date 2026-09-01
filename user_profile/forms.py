from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateUsernameForm(forms.Form):
    username = forms.CharField(
        label="نام کاربری جدید",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "نام کاربری جدید را وارد کنید",
            "class": "form-control",
        })
    )

    password = forms.CharField(
        label="رمز عبور فعلی",
        required=True,
        widget=forms.PasswordInput(attrs={
            "placeholder": "رمز عبور فعلی را وارد کنید",
            "class": "form-control",
        })
    )
class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(
        label="نام",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام خود را وارد کنید"
        })
    )

    last_name = forms.CharField(
        label="نام خانوادگی",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام خانوادگی خود را وارد کنید"
        })
    )

    email = forms.EmailField(
        label="ایمیل",
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "ایمیل خود را وارد کنید"
        })
    )

    password = forms.CharField(
        label="رمز عبور فعلی",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "رمز عبور فعلی را وارد کنید"
        })
    )


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label="رمز عبور فعلی",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "رمز عبور فعلی"
        })
    )

    new_password = forms.CharField(
        label="رمز عبور جدید",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "رمز عبور جدید"
        })
    )

    confirm_password = forms.CharField(
        label="تکرار رمز عبور جدید",
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "تکرار رمز عبور جدید"
        })
    )

    def clean(self):
        cleaned_data = super().clean()

        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError(
                    "رمز عبور جدید و تکرار آن یکسان نیستند."
                )

        return cleaned_data

class DeleteAccountForm(forms.Form):
    confirm = forms.BooleanField(
        required=True
    )

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-c',
            'placeholder': 'نام خود را وارد کنید'
        })
    )

    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-c',
            'placeholder': 'نام خانوادگی خود را وارد کنید'
        })
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'class': 'form-c',
            'placeholder': 'ایمیل خود را وارد کنید'
        })
    )

    username = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-c',
            'placeholder': 'نام کاربری خود را وارد کنید'
        })
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-c',
            'placeholder': 'پسورد خود را وارد کنید'
        })
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-c',
            'placeholder': 'دوباره پسورد خود را وارد کنید'
        })
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="نام کاربری",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "نام کاربری خود را وارد کنید",
            "class": "form-control",
        })
    )

    password = forms.CharField(
        label="رمز عبور ",
        required=True,
        widget=forms.PasswordInput(attrs={
            "placeholder": "رمز عبور خود را وارد کنید",
            "class": "form-control",
        })
    )
