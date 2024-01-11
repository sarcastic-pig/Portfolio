from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(subject, message, from_email, ["hablequentin@gmail.com"])
            return redirect('thanks/')
    else:
        form = ContactForm()
    
    return render(request, "homepage/index.html",  {"form":form} )


def thanks(request):
    return HttpResponse("Success!")

