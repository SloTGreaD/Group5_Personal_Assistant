from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'birthday']
        error_messages = {
            'phone_number': {
                'invalid': "Please enter a valid phone number.",
            },
            'email': {
                'invalid': "Please enter a valid email address.",
            },
        }


        
