"""
__author__ : "Sagar"
Purpose    :  "home page"
"""

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def home(request):
	"""
	Home page
	template = base.html
	params : request
	return : template
	"""
	template = "base.html"
	return render_to_response(template, {"test":"test"})