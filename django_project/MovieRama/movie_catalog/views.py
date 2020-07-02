from django.shortcuts import render, redirect
from .models import Movie
from django.views.decorators.csrf import csrf_protect
from .forms import CreateMovieForm
import datetime


def base(request):
	return render(request, "movie_catalog/base.html", {})

def index(request):
	movie_list = Movie.objects.all()
	return render(request, "movie_catalog/index.html", {"movie_list":movie_list})

@csrf_protect 
def create_movie(request):
	if request.method == "POST":
		form = CreateMovieForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data["title"]
			description = form.cleaned_data["description"]
			user = request.user 
			movie_record = Movie(title=title, user=user, description=description, date=datetime.datetime.now().date())
			movie_record.save()
			return redirect('/index')
	else:
		form = CreateMovieForm(request.POST)

	return render(request, "movie_catalog/create_movie.html", {'form':form})
