from django.shortcuts import render_to_response
from django.shortcuts import render
from django.core.context_processors import csrf
from gimmeapp.models import Post
from gimmeapp.models import User
from gimmeapp.models import Comment
from gimmeapp.models import Like
from gimmeapp.models import Lottery
from django.template import RequestContext

def preform(request):
	return render_to_response('preforms/form/form.html' )

def create_post(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST': # If the form has been submitted...
		form = PostForm(request.POST) # A form bound to the POST data
	#if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
	#		return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
	        form = PostForm() # An unbound form
	p = Post.objects.create()
	p.name = form.element_2
	p.user_created = form.element_1
	p.save()
	p.update(csrf(request))
	postlist = Post.objects.all()
	return render_to_response('allposts.html', c )

def view_post(request,post):
	p = Post.objects.get(id=post.id)
	return render_to_response('post.html', {  "post":p } )

def view_all_posts(request):
	postlist = Post.objects.all()
	if (len(postlist)==0):
		p = Post.objects.create(name="primo")
		p.save()
		postlist.append(p)	
	return render_to_response('allposts.html', { "postlist":postlist } )

def edit_post(request,post):
	p = Post.objects.get(id=post.id)
        return render_to_response('edit_post.html', {  "post":p } )

def hello_world(request,word):
	return render_to_response('hellow.html', { "word":word } )
