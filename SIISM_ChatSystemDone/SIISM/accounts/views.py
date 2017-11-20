from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'accounts/home.html', {})
	#return HttpResponse("This will be the home page")
	
