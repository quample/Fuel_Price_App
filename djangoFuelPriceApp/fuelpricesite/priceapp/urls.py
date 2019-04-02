from django.urls import path
from . import views
from priceapp.views import output_quote_history

urlpatterns = [
    path('', views.index, name='index'),
    path('profileupdate/',views.ProfileUpdate.as_view(), name = 'profileupdate'),
    #path('client_profile/', views.ClientProfileView.as_view(), name='client_profile'),
    path('client_profile/', views.client_profile,  name='client_profile'),
    #path('get_quote/', views.GetQuoteView.as_view(), name='get_quote'),
    path('get_quote/', views.get_quote, name='get_quote'),
    path('quote_history/', views.output_quote_history, name = 'quote_history'),
    path('signup/', views.SignUp.as_view(), name='signup'),
   
]