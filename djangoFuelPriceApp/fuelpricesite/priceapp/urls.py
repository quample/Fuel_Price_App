from django.urls import path
from . import views
from priceapp.views import output_quote_history

urlpatterns = [
    path('', views.index, name='index'),
    path('profileupdate/',views.client_profile_exists, name = 'profileupdate'),
    path('client_profile/', views.client_profile,  name='client_profile'),
    path('get_quote/', views.get_quote, name='get_quote'),
    path('quote_redirect/',views.pricing_redirect, name = 'quote_redirect'),
    path('quote_submit/',views.pricing_submit, name = 'quote_submit'),
    path('quote_history/', views.output_quote_history, name = 'quote_history'),
    path('signup/', views.SignUp.as_view(), name='signup'),
   
]