from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required = True, max_length = 100)
    email = forms.EmailField(required = True, max_length = 100)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,11}$')
    comment = forms.CharField(widget=forms.Textarea, label='Your Message')
