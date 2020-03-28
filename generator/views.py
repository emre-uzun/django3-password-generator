from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View

# Create your views here.

# deger almak icin, render 3 paramtre alabilir: {'password':'test1234'}

class passwordGenerator(View):
	isim = ""
	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello, World!')
	def anasayfa(self,request):
		return render(request, "generator/newhome.html" )



def anasayfa(request):
	return render(request, "generator/home.html" )


def password(request):

	characters = list("qwertyopasdfhjklzxcvbnm")
	numbersList = list("1234567890")
	uppercaseList = list("QWERTYOPASDFGHJKLZXCVBNM")
	specialList = list("!+%&?.,")


	#length = 10
	length = int(request.GET.get('length',12))

	if request.GET.get('uppercase'):
		characters.extend(list("QWERTYOPASDFGHJKLZXCVBNM"))
	if request.GET.get('numbers'):
		characters.extend(list("1234567890"))
	if request.GET.get('special'):
		characters.extend(list("!+%&?.,"))

	thePassword = ""

	for x in range(length):
		thePassword += random.choice(characters)

	return render(request, "generator/password.html", {'password':thePassword})