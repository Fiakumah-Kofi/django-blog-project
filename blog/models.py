from django.db import models
from django.contrib import admin

# Create your models here.

class Post(models.Model):
 	title =  models.CharField(max_length =60)	#(60 characters)
	body = models.TextField()	#(large text)
 	created = models.DateField ()	#(date created)
 	updated = models.DateField ()	#(date updated)
 	def __unicode__(self):
		return self.title
	@models.permalink
	def get_absolute_url(self):
		return ('post_detail',(),{'id':self.id,'showComments':'true/'})


class Comment(models.Model):
 	body = models.TextField()	#(large text)
 	author= models.CharField(max_length = 60)	#(60 characters)
 	created= models.DateField() 	#(date created)
 	updated = models.DateField() 	#(date updated)
 	post= models.ForeignKey (Post,related_name = 'message posted')		#(foreign key linking Comment to Post)
	def body_60(self):
		return self.body[:60]
	def __unicode__(self):
		return self.author
class CommentInline(admin.TabularInline):
	model=Comment

class PostAdmin(admin.ModelAdmin):
	list_display =('title','created','updated')
	search_fields=('title','body')
	list_filter=('created',)
	inlines = [CommentInline]

	
	

class CommentAdmin(admin.ModelAdmin):
	list_display = ('post','author','body_60','created','updated')
	list_filter =('created','updated')


 
	

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

