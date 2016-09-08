from django import forms
from .models import UserRegis

class UserRegisForm(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model=UserRegis
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
            ]
