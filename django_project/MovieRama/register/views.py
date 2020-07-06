from django.shortcuts import render, redirect 
from .forms import RegisterForm  
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect 
def register(response):
	#add new user
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
	else:
		form = RegisterForm(response.POST)

	return render(response, "register/register.html", {'form':form})

	