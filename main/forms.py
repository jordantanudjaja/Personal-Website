from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}))
