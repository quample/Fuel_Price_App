from django import forms

STATE_CHOICE = [
    ('TX','Texas'),
    ('CA','California'),
]
class ClientProfileForm(forms.Form):
    full_name = forms.CharField(max_length=50,strip=True)
    address_1 = forms.CharField(max_length=100,strip=True)
    address_2 = forms.CharField(max_length=100,strip=True,required=False)
    city = forms.CharField(max_length=100,strip=True)
    state = forms.CharField(widget = forms.Select(choices=STATE_CHOICE))
    zip_code = forms.CharField(max_length=9, min_length=5, strip=True)

#class GetQuoteForm(forms.Form):
