from django.shortcuts import render_to_response
from gimmeapp.models import Post
from gimmeapp.models import User
from gimmeapp.models import Comment
from gimmeapp.models import Like
from gimmeapp.models import Lottery

def create_post(request,created_by,postname):
	p = Post.objects.create()
	p.name = postname
	p.user_created = created_by
	p.save()
	return render_to_response('post.html', { "post":p } )

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
