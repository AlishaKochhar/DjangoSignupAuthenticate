from django import forms
from UserRegis.models import UserRegisForm
from .models import authent

class authentForm(forms.ModelForm) :
    class Meta :
        model=UserRegis
        fields=[
            'username',
            'password'
            ]
        
