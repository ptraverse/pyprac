from django.shortcuts import render_to_response
from simpletest.models import Ad
from simpletest.models import Person


def view_ad(request,user,ad):
	u = Person.objects.get(id__exact=user)
	a = Ad.objects.get(id__exact=ad)
	u.pc += a.point_worth
	u.Save()
	return render_to_response('adviewer.html', { "user":u , "ad":a } )

def create_ad(request,points,cost):
	a = Ad.create()
	a.points_worth = points
	a.ppv_cost = cost
	a.Save()
	return render_to_response('adviewer.html', {"ad":a})

def create_user(request,name):
	u = Person.create()
	u.name = name
	u.Save()
	return render_to_response('adviewer.html', {"user":u} )

def home(request):
	p = Person.objects.all()
	a = Ad.objects.all()
	return render_to_response('home.html', { "personlist":p , "adlist":a} )
