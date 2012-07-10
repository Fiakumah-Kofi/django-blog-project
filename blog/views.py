"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    output=''
    for stuff  in post_list :
	output+= str(stuff.title) + str(stuff.body) + str(stuff.id)+"<br>"
    return HttpResponse(output)


def post_detail(request, id, showComments=False):
    number= Post.objects.get(id=id)
    comment =''
    if (showComments != None):
	comment = Comment.objects.filter(post=id)
	return HttpResponse(comment)

    return HttpResponse(number)
    
def post_search(request, term):
   anything = Post.objects.filter(body_contains= term)
   return HttpResponse(anything)


def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') # Create your views here.
