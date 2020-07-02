from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Movie(models.Model):
	"""Model representing a Movie entity"""
	title = models.CharField(max_length=200)
	description = models.TextField(help_text='Enter a brief description of the movie')
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	date = models.DateField()
	hates = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	def __str__(self):
		"""String for representing the Model object."""
		return self.title

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('movie-detail', args=[str(self.id)])	



# class User(models.Model):
# 	"""Model representing user entity"""
# 	name = models.CharField(primary_key=True, max_length=100)
# 	email = models.EmailField(max_length=100,blank=True, null= True, unique= True)
# 	password = models.CharField(max_length=100)

# 	def get_absolute_url(self):
#         """Returns the url to access a particular author instance."""
#         return reverse('author-detail', args=[str(self.id)])
	
# 	def get_absolute_url(self):
#         """Returns the url to access a particular author instance."""
#         return reverse('user-detail', args=[str(self.name)])

#     def __str__(self):
#         """String for representing the Model object."""
#         return self.name