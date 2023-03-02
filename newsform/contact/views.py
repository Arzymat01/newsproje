from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('the form was valid')

            send_mail('The contact form subject', 'This is the message',
                      'arzymatarkabaev01@gmail.com', ['arzymatarkabaev01@gmail.com'])

            return redirect('contact')
        else:
            form = ContactForm()

    form = ContactForm()
    return render(request, "contact/contact.html", {
        'form': form
    })
