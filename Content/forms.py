from django import forms
from .models import PostsModel
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


# class CreatePostForm(forms.ModelForm):

#     """Form for create a new post"""

#     class Meta:
#         model = PostsModel
#         fields = ("topic", "message", "media")

#     def save(self, commit=True):
#         post = super(CreatePostForm, self).save(commit=False)
#         if commit:
#             post.save()
#         return post


class CreatePostForm(forms.Form):
    foo = SummernoteTextFormField()

    class Meta:
        model = PostsModel
        fields = ("topic", "message", "media")

    def save(self, commit=True):
         post = super(CreatePostForm, self).save(commit=False)
         if commit:
             post.save()
         return post


class FormForPostModel(forms.ModelForm):
    foo = SummernoteTextField()
