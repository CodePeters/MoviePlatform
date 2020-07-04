from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateMovieForm
from .models import Movie, Review
from django.db import transaction
from django.db.models import F
import datetime
import logging


logger = logging.getLogger(__name__)

def base(request):
	return render(request, "movie_catalog/base.html", {})

@csrf_protect 
def index(request):
	# if request.user.is_authenticated: current_user = request.user.id
	if request.method == "POST":
		user_id = request.POST.get("user", "")
		movie_id = request.POST.get("movie", "")
		button = request.POST.get("button", "")
		make_transactions(user_id, movie_id, button)
		return redirect('/index')
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

@csrf_protect
def profile(request, usrname):
	if request.method == "POST":
		user_id = request.POST.get("user", "")
		movie_id = request.POST.get("movie", "")
		button = request.POST.get("button", "")
		make_transactions(user_id, movie_id, button)
		return redirect('/index')
	movie_list = Movie.objects.filter(user__username=usrname)
	return render(request, "movie_catalog/index.html", {"movie_list":movie_list})

def make_transactions(user_id, movie_id, button):
	user = User.objects.get(id=user_id)
	movie = Movie.objects.get(id=movie_id)
	with transaction.atomic():
		if button == 'Like':
			review_record = Review(user=user, movie=movie, review='L')
			review_record.save()
			Movie.objects.filter(id=movie_id).update(likes=F('likes') + 1)
		elif button == 'Hate':
			review_record = Review(user=user, movie=movie, review='H')
			review_record.save()
			Movie.objects.filter(id=movie_id).update(hates=F('hates') + 1)
		elif button == 'UnLike':
			Review.objects.filter(user=user, movie=movie).delete()
			Movie.objects.filter(id=movie_id).update(likes=F('likes') - 1)
		elif button == 'UnHate':
			Review.objects.filter(user=user, movie=movie).delete()
			Movie.objects.filter(id=movie_id).update(hates=F('hates') - 1)

