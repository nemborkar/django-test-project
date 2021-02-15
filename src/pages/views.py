from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"history": "It all starts with the invention of fire",
		"year": "10000BC",
		"people": 4,
		"list": [2314,654,765,345]
	}
	return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contacts page</h1>")