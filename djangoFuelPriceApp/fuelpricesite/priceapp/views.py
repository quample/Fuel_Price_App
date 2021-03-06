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
from .forms import ClientProfileExists
from .forms import GetQuoteForm

#QuerySet
from django.db.models import Q

#Messages
from django.contrib import messages

#@login_required
def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    if request.META.get('HTTP_REFERER'):
        previous_page = request.META['HTTP_REFERER']
        print(previous_page)
        if 'quote_redirect' in previous_page and request.user.is_authenticated:
            UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last().delete()
            print("last user record deleted")
        elif 'quote_redirect' in previous_page and not request.user.is_authenticated:
            print(str(UserQuotes.objects.order_by('order_id').last()) + "DELETED")
            UserQuotes.objects.order_by('order_id').last().delete()
            print(str(UserQuotes.objects.order_by('order_id').last()) + "is last.")
        previous_page = "/priceapp/"
    return render(request, 'index.html')

class ProfileUpdate(LoginRequiredMixin,TemplateView):
    template_name = 'profileupdate.html'

@login_required(login_url='/accounts/login/')
def client_profile(request):
    if request.META.get('HTTP_REFERER'):
        previous_page = request.META['HTTP_REFERER']
        print(previous_page)
        if 'quote_redirect' in previous_page and request.user.is_authenticated:
            UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last().delete()
            print("last user record deleted")
        elif 'quote_redirect' in previous_page and not request.user.is_authenticated:
            print(str(UserQuotes.objects.order_by('order_id').last()) + " DELETED")
            UserQuotes.objects.order_by('order_id').last().delete()
            print(str(UserQuotes.objects.order_by('order_id').last()) + " is last.")
        previous_page = "/priceapp/client_profile/"
    if UserAddresses.objects.filter(user_name=request.user.username).exists():
        return HttpResponseRedirect('/priceapp/profileupdate/')
    else:
        if request.method == 'POST':
            form = ClientProfileForm(request.POST)
            if form.is_valid():
                fs=form.save(commit=False)
                fs.user_name=request.user.username
                fs.user=request.user
                fs.save()
                return HttpResponseRedirect('/priceapp/profileupdate/')
            elif form.has_error:
                messages.error(request, form.errors)
                return HttpResponseRedirect('/priceapp/client_profile/')                
        else:
            form = ClientProfileForm()
        context = {
            'form': form,
        }
        return render(request,'client_profile.html',context=context)

def client_profile_exists(request):
    if 'logout' in request.POST:
        messages.success(request,"User Logged out")
        return HttpResponseRedirect('/priceapp/')
    if UserAddresses.objects.filter(user_name=request.user.username).exists():
        if request.method == 'POST':                
            if 'edit' in request.POST:
                UserAddresses.objects.filter(user_name=request.user.username).delete()
                messages.success(request,"Client Profile reseted.")
                return HttpResponseRedirect('/priceapp/client_profile/')
        else:
            user_record = get_object_or_404(UserAddresses,user_name=request.user.username)
            form = ClientProfileExists(initial={
                'full_name':user_record.full_name,
                'ad_P':user_record.ad_P,
                'ad_P2':user_record.ad_P2,
                'ad_City':user_record.ad_City,
                'ad_State':user_record.ad_State,
                'ad_Zip':user_record.ad_Zip})
        context = {
            'form': form,
        }
        return render(request,'profileupdate.html',context=context)
    else:
        return HttpResponseRedirect('/priceapp/')

class GetQuoteView(LoginRequiredMixin, TemplateView):
    template_name = 'get_quote.html'

@login_required(login_url='/accounts/login/')
def get_quote(request):
    if request.META.get('HTTP_REFERER'):
        previous_page = request.META['HTTP_REFERER']
        print(previous_page)
        if 'quote_redirect' in previous_page:
            print(str(UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last()) + " DELETED")
            UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last().delete()
            print(str(UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last()) + " is now last.")
        previous_page = "/priceapp/get_quote/"
    if UserAddresses.objects.filter(user_name=request.user.username).exists():
        user_record = get_object_or_404(UserAddresses,user_name=request.user.username)
        delivery_address = {'delivery_address':user_record.ad_full}
        if request.method == 'POST':
            form = GetQuoteForm(request.POST,  initial=delivery_address)
            if form.is_valid():
                if 'quote' in request.POST:
                    fs=form.save()
                    fs.user_name=request.user.username
                    fs.user=request.user
                    fs.save()
                    messages.info(request,"Please Look at the Calculated Price, click SUBMIT to accept or click RESET QUOTE to enter new quote.")                    
                    return HttpResponseRedirect('/priceapp/quote_redirect/')
            elif form.has_error:
                messages.error(request, form.errors)
                return HttpResponseRedirect('/priceapp/get_quote/')                 
        else:
            form = GetQuoteForm(initial=delivery_address)
        context = {
            'form': form,
        }
        return render(request,'get_quote.html',context=context)
    else:
        messages.error(request, "No Client Address Found, please fill out your profile.")
        return HttpResponseRedirect('/priceapp/client_profile/')

def pricing_redirect(request):
    if UserQuotes.objects.filter(user_name=request.user.username).exists():
        user_record = UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last()
        delivery_address = {'delivery_address':user_record.delivery_address}    
        if request.method == 'POST':
            form = GetQuoteForm(request.POST,  initial=delivery_address)
            user_record.delete()
            if form.is_valid(): 
                if 'reset' in request.POST:
                    messages.error(request, "Quote submission discarded.")
                    return HttpResponseRedirect('/priceapp/quote_submit/')
                elif 'submit' in request.POST:
                    fs=form.save()
                    fs.user_name=request.user.username
                    fs.user=request.user
                    fs.save()
                    messages.success(request, "Quote submission was a success!")
                    return HttpResponseRedirect('/priceapp/quote_submit/')
        else:
            form = GetQuoteForm(initial={
                'reqGallons':user_record.reqGallons,
                'reqDelDate':user_record.reqDelDate,
                'delivery_address':user_record.delivery_address,
                'pricePerGal':user_record.pricePerGal,
                'totalPrice':user_record.totalPrice})
        context = {
            'form': form,
        }
        return render(request,'quote_redirect.html',context=context)
    else:
        return HttpResponseRedirect('/priceapp/get_quote/')

def pricing_submit(request):
    return render(request,'quote_submit.html')

class QuoteHistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'quote_history.html'

@login_required(login_url='/accounts/login/')
def output_quote_history(request):
    if request.META.get('HTTP_REFERER'):
        previous_page = request.META['HTTP_REFERER']
        if 'quote_redirect' in previous_page:
            print(str(UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last()) + " DELETED")
            UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last().delete()
            print(str(UserQuotes.objects.filter(user_name=request.user.username).order_by('order_id').last()) + " is now last.")
    if UserAddresses.objects.filter(user_name=request.user.username).exists():
        quotes = UserQuotes.objects.filter(user_name=request.user.username)
        obj = {
            'quote_list':quotes
        }
        return render(request,'quote_history.html',obj)
    else:
        return HttpResponseRedirect('/priceapp/')
    
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

