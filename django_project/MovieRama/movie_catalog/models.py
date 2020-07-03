from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import datetime

class Movie(models.Model):
	"""Model representing a Movie entity"""
	title = models.CharField(max_length=200)
	description = models.TextField(help_text='Enter a brief description of the movie')
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	date = models.DateField("date published")
	hates = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	def get_date(self):
          timenow = datetime.datetime.now().date()
          return (timenow-self.date).days

	def __str__(self):
		"""String for representing the Model object."""
		return self.title

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('movie-detail', args=[str(self.id)])	

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	role = models.ForeignKey(Movie, on_delete=models.PROTECT)
	options = (
		('L', 'likes'),
		('H', 'hates'),
	)
	review = models.CharField(max_length=1, choices=options)
