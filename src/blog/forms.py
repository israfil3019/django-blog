from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = {
            "title",
        }
        labels = {"title": "Name"}
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
        }
