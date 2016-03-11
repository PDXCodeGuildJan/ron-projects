from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def zengarden_index(request):

	#return an httpresponse of object using the render function
	return render(request, 'zengarden/zen_mockup.html')