from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages


@login_required
def home(request):
    return render(request, "home.html", {})
