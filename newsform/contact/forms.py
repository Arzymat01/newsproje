from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
