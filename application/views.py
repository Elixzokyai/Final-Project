from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ApplicationUserForm


def application_view(request):
    if request.method == 'POST':
        form = ApplicationUserForm(request.POST)
        if form.is_valid():
            # Save the user/application
            user = form.save()

            # Send an email notification
            subject = 'Welcome to blogger website'
            message = f'Dear {user.name},\n\nYour application has been received. Your status is currently pending. We will notify you once it has been approved.'
            recipient_email = user.email

            send_mail(
                subject,
                message,
                'elijahkyai100@gmail.com',
                [recipient_email],
                fail_silently=True,
            )

            return redirect('application_form')
    else:
        form = ApplicationUserForm()

    return render(request, 'application/application.html', {'form': form})

def application_form(request):
    return render(request, 'application/application_form.html')

