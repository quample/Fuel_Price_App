from django.urls import path

from . import views
from .views import HomePageView, ClientProfileView, GetQuoteView, LoginView, QuoteHistoryView, SignupView

urlpatterns = [
    path('', views.index, name='index'),
    path('home_page.html', HomePageView.as_view(),name='home'),
    path('client_profile.html',ClientProfileView.as_view(),name = 'clientprofile'),
    path('get_quote.html',GetQuoteView.as_view(),name = 'getquote'),
    path('login.html',LoginView.as_view(), name = 'login'),
    path('signup.html',SignupView.as_view(),name = 'signup'),
    path('quote_history.html',QuoteHistoryView.as_view(), name = 'quotehistory'),

]
