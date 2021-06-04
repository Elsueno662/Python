import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get('password1')


        if not re.search("[a-z]", password1):
            raise forms.ValidationError('Password must contain at least 1 alphabet')

        if not re.search("[A-Z]", password1):
            raise forms.ValidationError('Password must contain at least 1 uppercase alphabet')

        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password1):
            raise forms.ValidationError("Password must contain at least 1 special character")



