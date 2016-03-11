from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def price_list_index(request):

	#return an httpresponse of object using the render function
	return render(request, 'price_list/pricing_raw.html')