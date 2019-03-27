from django import forms
from priceapp.models import  UserAddresses,UserQuotes

STATE_CHOICE = [
    ('TX','Texas'),
    ('CA','California'),
    ('AL','Alabama'),
    ('AK','Alaska'),
    ('AZ','Arizona'),
    ('AR','Arkansas'),
    ('CA','California'),
    ('CO','Colorado'),
    ('CT','Connecticut'),
    ('DE','Delaware'),
    ('DC','District of Columbia'),
    ('FL','Florida'),
    ('GA','Georgia'),
    ('HI','Hawaii'),
    ('ID','Idaho'),
    ('IL','Illinois'),
    ('IN','Indiana'),
    ('IA','Iowa'),
    ('KS','Kansas'),
    ('KY','Kentucky'),
    ('LA','Louisiana'),
    ('ME','Maine'),
    ('MD','Maryland'),
    ('MA','Massachusetts'),
    ('MI','Michigan'),
    ('MN','Minnesota'),
    ('MS','Mississippi'),
    ('MO','Missouri'),
    ('MT','Montana'),
    ('NE','Nebraska'),
    ('NV','Nevada'),
    ('NH','New Hampshire'),
    ('NJ','New Jersey'),
    ('NM','New Mexico'),
    ('NY','New York'),
    ('NC','North Carolina'),
    ('ND','North Dakota'),
    ('OH','Ohio'),
    ('OK','Oklahoma'),
    ('OR','Oregon'),
    ('PA','Pennsylvania'),
    ('RI','Rhode Island'),
    ('SC','South Carolina'),
    ('SD','South Dakota'),
    ('TN','Tennessee'),
    ('TX','Texas'),
    ('UT','Utah'),
    ('VT','Vermont'),
    ('VA','Virginia'),
    ('WA','Washington'),
    ('WV','West Virginia'),
    ('WI','Wisconsin'),
    ('WY','Wyoming'),    
]

class ClientProfileForm(forms.ModelForm):
    """class Meta:
        model = UserAddresses
      
    full_name = forms.CharField(max_length=50,strip=True)
    address_1 = forms.CharField(max_length=100,strip=True)
    address_2 = forms.CharField(max_length=100,strip=True,required=False)
    city = forms.CharField(max_length=100,strip=True)
    state = forms.CharField(widget = forms.Select(choices=STATE_CHOICE))
    zip_code = forms.CharField(max_length=9, min_length=5, strip=True)
    """  
    class Meta:
        model = UserAddresses
        exclude = ['user','ad_full']


class GetQuoteForm(forms.Form):
    Gallons = forms.IntegerField()
#    Delivery_Date = forms.DateField()
