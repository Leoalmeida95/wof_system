from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Usuario


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'id': 'password'}))
    password2 = forms.CharField(label='password_confirm', widget=forms.PasswordInput(attrs={'id': 'password_confirm'}))
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'id': 'first_name'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'id': 'last_name'}))
    cpf = forms.CharField(label='cpf', widget=forms.TextInput(attrs={'id': 'cpf'}))
    conta_publica = forms.CharField(label='conta_publica', widget=forms.BooleanField)
    formacao = forms.CharField(label='formacao', widget=forms.TextInput(attrs={'id': 'formacao'}))
    profissao = forms.CharField(label='profissao', widget=forms.TextInput(attrs={'id': 'profissao'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'id': 'email'}))
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','cpf','conta_publica','formacao','profissao', 'email']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ['first_name','last_name','cpf','conta_publica','formacao','profissao', 'email','is_activeUser', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]