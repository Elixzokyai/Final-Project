from django.shortcuts import render
from  django.shortcuts import render, redirect

from .forms import ApplicationUserForm

# Create your views here.

def  application_view(request):
    if request.method == 'POST':
        form = ApplicationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_form')
    else:
        form = ApplicationUserForm()
        return render(request, 'application/application.html', {'form': form})


def application_form(request):
    return render(request, 'application/application_form.html')