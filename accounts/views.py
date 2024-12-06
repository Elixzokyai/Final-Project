from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import BlogUserCreationForm
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from .models import BlogUser


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = BlogUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_registration_email(user)
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed')
    else:
        form = BlogUserCreationForm()

    # Always return the form in the response, whether POST or GET
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('blogapp')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')


@login_required()
def home_view(request):
    return render(request, 'accounts/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def send_registration_email(user):
    try:
        subject = 'Welcome to Our blogger.com!'
        message = f'Hello {user.username},\n\nThank you for registering at our website.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

        print("Successful registration")

    except Exception as e:
        print(f"Error sending email: {e}")
