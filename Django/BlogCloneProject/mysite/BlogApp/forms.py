from django import forms
from BlogApp.models import Post, Comment


# Create your forms here.
class PostForm(forms.ModelForm):
    class meta():
        model = Post
        fields = ('author', 'title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-edited-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class meta():
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
