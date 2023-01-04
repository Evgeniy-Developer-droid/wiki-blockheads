from django.contrib import admin
from .models import PostsModel, CommentsModel


admin.site.register(PostsModel)
admin.site.register(CommentsModel)

