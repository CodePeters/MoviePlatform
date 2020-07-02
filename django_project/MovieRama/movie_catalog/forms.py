from django import forms

class CreateMovieForm(forms.Form):
	title = forms.CharField(label="title ", max_length=200)
	description = forms.CharField(widget=forms.Textarea, label="description ")
