from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import CustomUser


class CreateUserForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')