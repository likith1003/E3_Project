from django import forms
from .models import *

# create a forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {'password': forms.PasswordInput}
        help_texts = {'username':''}