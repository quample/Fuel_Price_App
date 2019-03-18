from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
     return render(request, 'home_page.html')

class HomePageView(TemplateView):
    template_name = 'home_page.html'

class ClientProfileView(TemplateView):
    template_name = 'client_profile.html'

class GetQuoteView(TemplateView):
    template_name = 'get_quote.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class QuoteHistoryView(TemplateView):
    template_name = 'quote_history.html'

class SignupView(TemplateView):
    template_name = 'signup.html'