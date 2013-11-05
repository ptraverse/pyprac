
from django import forms 
class PostForm(forms.Form):
	user_creating = forms.CharField(max_length=100)
	title = forms.CharField()
 	description  = forms.CharField()
	 # # # # price = forms.FloatField()
	# def is_valid(self):
		
