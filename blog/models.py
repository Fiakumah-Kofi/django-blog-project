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


class Comment(models.Model):
 	body = models.TextField()	#(large text)
 	author= models.CharField(max_length = 60)	#(60 characters)
 	created= models.DateField() 	#(date created)
 	updated = models.DateField() 	#(date updated)
 	post= models.ForeignKey (Post,related_name = 'message posted')		#(foreign key linking Comment to Post)
	def __unicode__(self):
		return self.author

admin.site.register(Post)
admin.site.register(Comment)

