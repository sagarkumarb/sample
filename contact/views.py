from django.shortcuts import render, render_to_response
from contact.forms import ContactForm


# Create your views here.
def contact(request):

    print "yes"
    template = "contact/contact_us.html"
    form = ContactForm()
    if request.method == "POST":
        print "yesssssss"
    return render_to_response(template, {"form":form},)