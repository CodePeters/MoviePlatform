from django.urls import path
from . import views

urlpatterns = [

	path("", views.index, name="view index"),
	path("create/", views.create_movie, name="view create_movie"),
	path("profile/<str:usrname>/", views.profile, name="view create_movie"),

]