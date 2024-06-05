from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def home(request):
    un = request.session.get('username')
    if un:
        user_object = User.objects.get(username=un)
        d = {'UO':user_object}
        return render(request, 'home.html', d)
    return render(request, 'home.html')


def customer_registration(request):
    ECFO = CustomerForm()
    d = {'ECFO': ECFO}
    if request.method == 'POST':
        CFDO = CustomerForm(request.POST)
        if CFDO.is_valid():
            pw = CFDO.cleaned_data['password']
            MCFDO = CFDO.save(commit=False)
            MCFDO.set_password(pw)
            MCFDO.save()
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('Invalid Data')
    return render(request, 'customer_registration.html', d)


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password = pw)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('Invalid Credentials')
    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))