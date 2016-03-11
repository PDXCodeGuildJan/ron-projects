from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def homepage_index(request):
	#print("test")
	#return an httpresponse of object using the render function
	return render(request, 'homepage/profile3.html')