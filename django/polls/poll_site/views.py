from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse


from .models import Question, Choice

# Create your views here.

def hello_world(request):
	# view controllers must always take an HttpRequest
	
	# always need to return an HttpResponse
	return HttpResponse("Hello World")

def hello_world_render(request):

	questions = Question.objects.all()
	#print(questions)

	#print(questions[0].id)
	#print(questions[0].questions_text)
	#print(questions[0].pub_date)


	context = {
	'questions': questions,

	}

	#return an httpresponse of the object using the render function
	return render(request, 'poll_site/index.html', context)


def corgi_page(request):
	return render(request, 'poll_site/corgi.html')


def question_details(request, question_id):

	print("passed question:", question_id)

	question = get_object_or_404(Question, pk=question_id)

	context = {
	'question': question,
	}

	return render(request, 'poll_site/question_details.html', context)