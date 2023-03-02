from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contact_us
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        contact = Contact_us()
        ful_name = request.POST.get('ful_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact.full_name = ful_name
        contact.email = email
        contact.subject = subject
        contact.phone = phone
        contact.message = message
        contact.save()
        return HttpResponse('<h1>Thanks for contact us</h1>')

    return render(request, 'contact/contact.html')
