# Create your views here

from django.shortcuts import render_to_response
from AllAboard.models import Animal

def home(request):
	return render_to_response('home.html',{"message":"welcome to the homepage motherfucker!"})
	
def legs(request,word):
	a = Animal.objects.all()
	return render_to_response('howmanylegs.html',{"animal_list":a})

		
