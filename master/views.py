from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

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
            return HttpResponse('master_registration is Dome')
    return render(request, 'master_registration.html', d)