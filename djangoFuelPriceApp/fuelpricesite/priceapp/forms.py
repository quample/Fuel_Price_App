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

class ClientProfileExists(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(ClientProfileExists, self).__init__(*args, **kwargs)
        self.fields['full_name'].disabled = True
        self.fields['ad_P'].disabled = True
        self.fields['ad_P2'].disabled = True
        self.fields['ad_City'].disabled = True
        self.fields['ad_State'].disabled = True
        self.fields['ad_Zip'].disabled = True
    class Meta:
        model = UserAddresses
        exclude = ['user','user_name','ad_full']

class ClientProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(ClientProfileForm, self).__init__(*args, **kwargs)
    class Meta:
        model = UserAddresses
        widgets = {
            'ad_State' : forms.Select(choices=STATE_CHOICE),
            'full_name' : forms.TextInput(attrs={'placeholder':'Enter full-name'})
        }
        exclude = ['user','user_name','ad_full']

class GetQuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(GetQuoteForm, self).__init__(*args, **kwargs)                       
        self.fields['delivery_address'].disabled = True
        self.fields['pricePerGal'].disabled = True
        self.fields['totalPrice'].disabled = True

    class Meta:
        model = UserQuotes
        widgets ={
            'reqDelDate':forms.DateInput(attrs={'class':'datepicker'}),
        }
        exclude = ['user','user_name','order_num']
