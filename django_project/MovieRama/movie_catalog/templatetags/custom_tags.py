from django import template
from movie_catalog.models import Movie, Review
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def user_likes_or_not(movie, user):
	query = Review.objects.filter(movie=movie, user=user, review='L').exists()
	return query

@register.simple_tag
def user_hates_or_not(movie, user):
	query = Review.objects.filter(movie=movie, user=user, review='H').exists()
	return query