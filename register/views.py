from django.shortcuts import render, HttpResponseRedirect
from .forms import Register

# Create your views here.

def register(request):
    if request.method == 'POST':
        reg = Register(request.POST)
        if reg.is_valid():
            reg.save()
            print('Hello world')
            return HttpResponseRedirect('/login')
    else:
        reg = Register()

    return render(request, 'register/register.html', {'form':reg})