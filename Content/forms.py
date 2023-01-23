from django import forms
from .models import PostsModel
from .custom_function import SummernoteTextFormField


class CreatePostForm(forms.ModelForm):
    topic = forms.CharField()
    message = SummernoteTextFormField()


    class Meta:
        model = PostsModel
        fields = ["topic", "message", "media_main_post"]

    def save(self, commit=True):
         post = super(CreatePostForm, self).save(commit=False)
         if commit:
             post.save()
         return post


class UpdatePostForm(forms.ModelForm):
    topic = forms.CharField()
    message = SummernoteTextFormField()

    class Meta:
        model = PostsModel
        fields = ["topic", "message", "media_main_post"]