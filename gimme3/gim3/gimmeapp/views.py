from django.shortcuts import render_to_response
from gimmeapp.models import Post
from gimmeapp.models import User
from gimmeapp.models import Comment
from gimmeapp.models import Like
from gimmeapp.models import Lottery

def view_post(request,post):
	p = Post.objects.get(id=post.id)
	return render_to_response('post.html', {  "post":p } )

def view_all_posts(request):
	postlist = Post.objects.all()
	return render_to_response('allposts.html', { "postlist":postlist } )

def edit_post(request,post):
	p = Post.objects.get(id=post.id)
        return render_to_response('edit_post.html', {  "post":p } )

