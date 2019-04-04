from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from priceapp.models import UserAddresses, UserQuotes
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

#Forms
from .forms import ClientProfileForm
from .forms import GetQuoteForm

#QuerySet
from django.db.models import Q

#@login_required
def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class ProfileUpdate(LoginRequiredMixin,TemplateView):
    template_name = 'profileupdate.html'

@login_required(login_url='/accounts/login/')
def client_profile(request):

    #profile_instance = get_object_or_404(UserAddresses)

    if request.method == 'POST':
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            fs=form.save(commit=False)
            fs.user_name=request.user.username
            fs.user=request.user
            fs.save()
            return HttpResponseRedirect('/priceapp/profileupdate/')
    else:
        user_record = get_object_or_404(UserAddresses,user_name=request.user.username)
        form = ClientProfileForm(initial={
            'full_name':user_record.full_name,
            'ad_P':user_record.ad_P,
            'ad_P2':user_record.ad_P2,
            'ad_City':user_record.ad_City,
            'ad_State':user_record.ad_State,
            'ad_Zip':user_record.ad_Zip})
    context = {
        'form': form,
     }
    return render(request,'client_profile.html',context=context)


class GetQuoteView(LoginRequiredMixin, TemplateView):
    template_name = 'get_quote.html'

@login_required(login_url='/accounts/login/')
def get_quote(request):
    user_record = get_object_or_404(UserAddresses,user_name=request.user.username)
    delivery_address = {'delivery_address':user_record.ad_full}
    if request.method == 'POST':
        form = GetQuoteForm(request.POST,  initial=delivery_address)
        if form.is_valid():
            fs=form.save()
            fs.user_name=request.user.username
            fs.user=request.user
            fs.save()
            return HttpResponseRedirect('/priceapp/get_quote/')
    else:
        form = GetQuoteForm(initial=delivery_address)
    context = {
        'form': form,
     }
    return render(request,'get_quote.html',context=context)

class QuoteHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'quote_history.html'

@login_required(login_url='/accounts/login/')
def output_quote_history(request):
    #user_record = get_object_or_404(UserQuotes,user_name=request.user.username)
    quotes = UserQuotes.objects.all()
    obj = {
        'quote_list':quotes
    }
    return render(request,'quote_history.html',obj)
    '''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

