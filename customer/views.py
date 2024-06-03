from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def home(request):
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
            return HttpResponse('customer_registration is Done')
    return render(request, 'customer_registration.html', d)