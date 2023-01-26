from django import forms
from .models import PostsModel
from .custom_function import SummernoteTextFormField


class CreatePostForm(forms.ModelForm):
    topic = forms.CharField()
    base = SummernoteTextFormField()
    gameplay = SummernoteTextFormField()
    growth = SummernoteTextFormField()
    latest_update = SummernoteTextFormField()


    class Meta:
        model = PostsModel
        fields = ["topic", "base", "gameplay", "growth", "latest_update", "media_main_post"]

    def save(self, commit=True):
         post = super(CreatePostForm, self).save(commit=False)
         if commit:
             post.save()
         return post


class UpdatePostForm(forms.ModelForm):
    topic = forms.CharField()
    base = SummernoteTextFormField()
    gameplay = SummernoteTextFormField()
    growth = SummernoteTextFormField()
    latest_update = SummernoteTextFormField()

    class Meta:
        model = PostsModel
        fields = ["topic", "base", "gameplay", "growth", "latest_update", "media_main_post"]