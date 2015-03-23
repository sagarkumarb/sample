from django.shortcuts import render
from contact.forms import ContactForm


# Create your views here.
def contact(request):
    template = "contact_us.html"
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            pass
    return render(request, template, {'form':form})