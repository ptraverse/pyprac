from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from gimmeapp.models import Post
from gimmeapp.models import User
from gimmeapp.models import Comment
from gimmeapp.models import Like
from gimmeapp.models import Lottery
from django.template import RequestContext
from gimmeapp.models import *
from gimmeapp.forms import PostForm
from django.contrib.auth import authenticate, login

def log_in(request):
	if request.method=='POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user is not None:
      	 		if user.is_active:
      	 			login(request, user)
				return HttpResponseRedirect('../allposts' )
		
	       	else:
			return HttpResponseRedirect('../sign-up')
	else:
		return render(request,'login.html' )
#def log_in(request):
	
			


def landing_page(request):
	return render_to_response('preforms/form/landing_page.html' )

def e404_page(request, othertext):
	return render_to_response('preforms/form/e404_page.html' )

def preform(request):
	return render_to_response('preforms/form/form.html' )

def new_post(request):
	return render(request,'preforms/form/new_post_form.html' )

def create_post(request):
	if request.method == 'POST': # If the form has been submitted...
		p = Post.objects.create()
		p.user_created = request.POST.get("element_1","")	
		p.name = request.POST.get("element_2","")
		p.description = request.POST.get("element_3","")
		# p.price = request.POST.get("element_4","")
		p.save()
        	postlist = Post.objects.all()
		return HttpResponseRedirect('../allposts')
	#else:
		#return HttpResponseRedirect('../sign-up')
	
def sign_up(request):
	return render(request,'preforms/form/sign_up_form.html' )

def view_post(request,post):
	p = Post.objects.get(id=post.id)
	return render_to_response('post.html', {  "post":p } )

def view_all_posts(request):
	postlist = Post.objects.all()
	if (len(postlist)==0):
		p = Post.objects.create(name="primo")
		p.save()
		postlist = [] 
		postlist.append(p)	
	return render_to_response('allposts.html', { "postlist":postlist } )

def edit_post(request,post):
	p = Post.objects.get(id=post.id)
        return render_to_response('edit_post.html', {  "post":p } )

def hello_world(request,word):
	if (word==''):
		word = 'DefaultWorldWord'
	return render_to_response('hellow.html', { "word":word } )
