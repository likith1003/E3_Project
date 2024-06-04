from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.


def master_registration(request):
    EMFO = MasterForm()
    d = {'EMFO': EMFO}
    if request.method == 'POST':
        MFDO = MasterForm(request.POST)
        if MFDO.is_valid():
            pw = MFDO.cleaned_data['password']
            MMFDO = MFDO.save(commit=False)
            MMFDO.set_password(pw)
            MMFDO.is_staff = True
            MMFDO.save()
            return HttpResponseRedirect(reverse('master_login'))
        return HttpResponse('Invalid Credentials')
    return render(request, 'master_registration.html', d)


def master_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password = pw)
        if AUO and AUO.is_active and AUO.is_staff:
            login(request, AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('invalid Credentials')
    return render(request, 'master_login.html')