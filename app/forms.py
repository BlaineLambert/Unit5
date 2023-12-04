from django import forms

class Contact_form(forms.Form):
    name = forms.CharField(required=True)
    number = forms.CharField(required=True)
    email = forms.CharField(required=True)
