from django.contrib import admin

# Register your models here.
from priceapp.models import  UserAddresses,UserQuotes

#admin.site.register( UserAddresses)
@admin.register(UserAddresses)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name','ad_State','ad_Zip')


#admin.site.register(UserQuotes)
@admin.register(UserQuotes)

class QuoteAdmin(admin.ModelAdmin):
    pass