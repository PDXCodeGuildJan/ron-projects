from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def javapic_index(request):

	#return an httpresponse of object using the render function
	return render(request, 'javapic/index.html')

def javapic_join(request):

	#return an httpresponse of object using the render function
	return render(request, 'javapic/join.html')

def javapic_gallery(request):

	#return an httpresponse of object using the render function
	return render(request, 'javapic/gallery.html')