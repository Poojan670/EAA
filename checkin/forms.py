from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    secret_key= forms.CharField(label='Secret key', max_length=100)
    