from django import forms
from django.forms import Textarea,ChoiceField,CharField,Select,TimeField,TextInput

from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'status',
        ]
        labels = {
            'title': 'Title ',
            'content':'Content ',
            'status':'Status ',
        }
        widgets = { 'title': TextInput(attrs={'class': "form-control",}),
                    'content': Textarea(attrs={'class': "form-control", 'aria-describedby': "basic-addon1",}),
                    'status': Select(attrs={'class': "form-control",}),
                    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {'content': Textarea(attrs={'class':"form-control",'aria-describedby':"basic-addon1",'cols':40,'rows':1}),}
        fields = [
            'content',
        ]
        labels = {
            'content': 'Comment ',
        }

