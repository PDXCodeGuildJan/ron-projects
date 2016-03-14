from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http.response import JsonResponse

import json


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

	context = {'question': question}

	return render(request, 'poll_site/question_details.html', context)



def submit_vote(request):
	"""Handles vote submissions via AJAX"""

	#print ("inside submit function")

	if request.method == 'POST':
		#decode request body from the bytecode to normal
		data_json = request.body.decode("utf-8")

		#converts data from string to object
		data = json.loads(data_json)

		# get the choice at that id
		choice = Choice.objects.get(pk=int(data['choice_id']))

		#increment the votes of the choice by 1
		choice.votes += 1

		#save the updated object choice to the database
		choice.save()

		#get all the choices for the question just voted on
		question = Question.objects.get(pk=int(data['question_id']))

		question_choices = question.choice_set.all()

		#Build the reponse data
		response = []

		#loop through the choices and add them to a dictionary
		for choice in question_choices:
			c_dict = {
			'id': choice.id,
			'text': choice.choice_text,
			'votes': choice.votes
			}

			response.append(c_dict)

		#response_json = json.dumps(response)

		#print(data)
		#print(choice)
		#print(question_choices)

	return JsonResponse({'data': response}) #takes python dict that returns a json string


