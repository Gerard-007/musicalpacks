from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required = True, max_length = 100)
    email = forms.EmailField(required = True, max_length = 100)
    comment = forms.CharField(required = True, )
