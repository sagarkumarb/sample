"""
__author__: Sakar
purpose   : Receive email
"""
from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=100 , widget = forms.TextInput(
                                                                    attrs= {'class': 'form-control', 'id': 'input_name', 'placeholder': 'Enter your name*',}))
    email = forms.EmailField(max_length=100, widget = forms.TextInput(
                                                                    attrs= {'class': 'form-control', 'id': 'input_email', 'placeholder': 'Enter your email*',}))