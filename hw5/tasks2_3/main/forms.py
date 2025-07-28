from django import forms
from main.fields import AnyCharField
from main.models import LogInModel

class SignUpForm(forms.Form):
    username = AnyCharField(max_length=255)
    mail = AnyCharField(max_length=255)
    password = AnyCharField(max_length=255)

class LogInForm(forms.Form):
    username = AnyCharField(max_length=255)
    password = AnyCharField(max_length=255)

class LogInModelForm(forms.ModelForm):
    class Meta:
        model = LogInModel
        fields = ['username', 'password']