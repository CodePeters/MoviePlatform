from django.shortcuts import render
#from .models import Movie, blah ...

# Create your views here.

def base(response):
	return render(response, "movie_catalog/base.html", {})

def index(response):
	return render(response, "movie_catalog/index.html", {})