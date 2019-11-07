from django import forms
from blackboard.models import Users
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ['username', 'phone_number', 'email', 'password1', 'password2']