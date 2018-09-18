from django import forms
from .models import Post
 
 
class CarBlogForm(forms.ModelForm):
 
    class Meta:
        model = Post
        fields = ('title', 'content','image') 