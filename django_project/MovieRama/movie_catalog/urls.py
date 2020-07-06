from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [

	path("", views.index, name="view index"),
	path("create/", views.create_movie, name="view create_movie"),
	path("profile/<str:usrname>/", views.profile, name="view profile"),
	path("profile/<str:usrname>/search/", views.search, name="view search"),
	re_path("search/", views.search, name="view search"),

]