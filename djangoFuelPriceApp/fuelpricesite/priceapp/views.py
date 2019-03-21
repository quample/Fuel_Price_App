from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
#from FuelPriceApp.models import Book, Author, BookInstance, Genre
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

#Forms
from .forms import ClientProfileForm
from .forms import GetQuoteForm

#@login_required
def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class ProfileUpdate(LoginRequiredMixin,TemplateView):
    template_name = 'profileupdate.html'

@login_required(login_url='/accounts/login/')
def client_profile(request):
    if request.method == 'POST':
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/priceapp/profileupdate/')
    else:
        form = ClientProfileForm()
    context = {
        'form': form,
     }
    return render(request,'client_profile.html',context=context)

"""
class ClientProfileView(LoginRequiredMixin, FormView,request):
    template_name = 'client_profile.html'

    if request.method == 'POST':
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/profileupdate/')
    else:
        form = ClientProfileForm()
"""
    

class GetQuoteView(LoginRequiredMixin, TemplateView):
    template_name = 'get_quote.html'

@login_required(login_url='/accounts/login/')
def get_quote(request):
    if request.method == 'POST':
        form = GetQuoteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/priceapp/get_quote/')
    else:
        form = GetQuoteForm()
    context = {
        'form': form,
     }
    return render(request,'get_quote.html',context=context)

class QuoteHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'quote_history.html'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

