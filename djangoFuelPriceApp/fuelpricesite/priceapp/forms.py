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
        exclude = ['user','user_name','ad_full']


class GetQuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(GetQuoteForm, self).__init__(*args, **kwargs)                       
        self.fields['delivery_address'].disabled = True

    class Meta:
        model = UserQuotes
        widgets ={
            'reqDelDate':forms.DateInput(attrs={'class':'datepicker'}),
        }
        exclude = ['user','user_name','order_num']
'''
class Output_QuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(Output_QuoteForm, self).__init__(*args, **kwargs)                       
        self.fields['delivery_address'].disabled = True
    
    class meta:
        model = UserQuotes
'''
'''
    order_id = models.AutoField(primary_key=True)
    reqGallons = models.CharField(max_length=10,verbose_name="Requested Gallons")
    reqDelDate = models.DateField(blank=False,verbose_name="Delivery Date",default="MM/DD/YYYY")
    delivery_address = models.CharField(max_length=300,verbose_name="Delivery Address")
'''
