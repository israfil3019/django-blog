from django import forms
from .models import Blog, Comment, Category

class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")


    class Meta:
        model = Blog
        widgets = {
            'text': forms.Textarea(attrs={'rows':'5', 'cols': '40'}),
        }
        fields = (
            'title',
            'text',
            'image',
            'category',
        )
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        