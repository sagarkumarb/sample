from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from contact.forms import ContactForm


# Create your views here.
def contact(request):
    template = "contact_us.html"
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            send_mail("Test mail", "Hi {}, This is the test mail".format(form.cleaned_data['name']),
                      settings.DEFAULT_FROM_EMAIL, [form.cleaned_data['email']], fail_silently= True)
            messages.success(request, "Mail sent successfully !")
    return render(request, template, {'form':form})