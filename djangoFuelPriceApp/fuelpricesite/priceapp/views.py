from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
#from FuelPriceApp.models import Book, Author, BookInstance, Genre
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required
def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class ClientProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'client_profile.html'

class GetQuoteView(LoginRequiredMixin, TemplateView):
    template_name = 'get_quote.html'

class QuoteHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'quote_history.html'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'