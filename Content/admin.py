from django.contrib import admin
from .models import PostsModel, CommentsModel
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('message',)


admin.site.register(PostsModel, PostAdmin)
admin.site.register(CommentsModel)

