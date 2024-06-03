from django import forms
from  .models import *
from django.contrib.auth.models import User

class MasterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username': ''}