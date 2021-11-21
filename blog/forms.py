from django import forms
from .models import Comments, Post


class NewCommentForm(forms.ModelForm):
    
	class Meta:
    		
		model = Comments
		fields = ['comment']




class NewPostForm(forms.ModelForm):
    	
	class Meta:
		model = Post
		fields = ['title','content' ]