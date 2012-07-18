"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from models import Comment



#def post_list(request):
 #   post_list = Post.objects.all()
  #  output=''
   # for stuff  in post_list :
	#output+= str(stuff.title) + str(stuff.body) + str(stuff.id)+"<br>"
  #  return HttpResponse(output)


class CommentForm(ModelForm):# this is to make sure that ur forms have the same model as your database in python 
	class Meta:# and they claim this is easier than the former i wonder how the former was
	    model = Comment
	    exclude=['post','updated','created']# lets you exlude the fields that you do not like
	



@csrf_exempt

def post_detail(request, id, showComments = False):
    post = Post.objects.get(pk=id)
    comment = Comment(post=post)
    comments=''
    if request.method == 'POST':	
  	form = CommentForm(request.POST, instance=comment)
	if form.is_valid():
            form.save()
	return HttpResponseRedirect(request.path)# bring you back to the same page
    else:
	form = CommentForm

   
    if (showComments != None):
	 comments = Comment.objects.filter(post=post)
	 
    return render_to_response('blog/post_detail.html',{'post': post, 'comments':comments,'form' :form})
    
def post_search(request, term):
    anything = Post.objects.filter(body__contains= term)
    return render_to_response('blog/post_search.html',{'post': anything})


#def home(request):
  #  print 'it works'
   # return HttpResponse('hello world. Ete zene?') # Create your views here.
#

def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')# this is going to link to the right html file
    c = Context({'posts':posts })# this is to link the right variable in templates
    return HttpResponse(t.render(c))


def home(request):
    return render_to_response('blog/base.html',{})
# please note that request is a default object that must be passed to all the view functions else nothing works 
# but something like request.Post 

@csrf_exempt

def edit_comment(request, id):
    comment = Comment.objects.get(pk=id)
    if request.method == 'POST':	
  	form = CommentForm(request.POST, instance=comment) # form is an object of the comment class 
                                                           #but with the saying that whatever you put on is comment
	if form.is_valid():                                # this mean if the form is valid when all the fields are filled with the required data
            form.save()
	return HttpResponseRedirect('/blog/posts/' + str(comment.post.id))# to redirect the stuff back to the comment page
    else:
	form = CommentForm(instance= comment)# return the comment you were filling to \
        #remomve the error urself otherwise it would return an empty form which is baddd

    return render_to_response('blog/edit_comment.html',{'post': comment,'form' :form})
     


