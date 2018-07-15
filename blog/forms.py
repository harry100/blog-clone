from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
	title = forms.CharField(required=True,
							 	widget=forms.TextInput(attrs={'class': 'textinputclass'}))

	text = forms.CharField(required=True,
							 	widget=forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}))
	class Meta():
		model = Post
		fields = ('author','title','text')
		# widgets = {
		# 	'title':forms.TextInput(attrs={'class':'textinputclass'})
		# 	'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})}


class CommentForm(forms.ModelForm):
	author = forms.CharField(required=True,
							 	widget=forms.TextInput(attrs={'class': 'textinputclass'}))
	
	text = forms.CharField(required=True,
							 	widget=forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}))
	class Meta():
		model = Comment
		fields = ('author','text')
		# widgets = {
		# 	'author':forms.TextInput(attrs={'class':'textinputclass'})
		# 	'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
		# }