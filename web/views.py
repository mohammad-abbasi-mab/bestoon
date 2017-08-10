from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from web.models import User, Dakhl, Kharj, Token
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
# Create your views here.
def submit_dakhl(request):
	"""user submits a DAKHL"""

	print ("SUBMIT_DAKHl")
	print (request.POST)
	this_token = request.POST['token']
	this_user = User.objects.filter(token__token = this_token).get()
	if 'date' not in request.POST:
		date = datetime.now()
	else:
		date = request.POST['date']

	Dakhl.objects.create(text = request.POST['text'], date = date, user = this_user, amount = request.POST['amount'])
	return JsonResponse((
		{'status' : 'ok'},
		),safe = False,  encoder = JSONEncoder)



@csrf_exempt
# Create your views here.
def submit_kharj(request):
	"""user submits a kharj"""

	print ("SUBMIT_KHARJ")
	print (request.POST)
	this_token = request.POST['token']
	this_user = User.objects.filter(token__token = this_token).get()
	if 'date' not in request.POST:
		date = datetime.now()
	else:
		date = request.POST['date']

	Kharj.objects.create(text = request.POST['text'], date = date, user = this_user, amount = request.POST['amount'])
	return JsonResponse((
		{'status' : 'ok'},
		),safe = False,  encoder = JSONEncoder)