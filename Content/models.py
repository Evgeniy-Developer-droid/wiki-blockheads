from django.db import models
from django.contrib.auth.models import User


class PostsModel(models.Model):

    """Post storage model"""

    timestamps = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255, default='')
    message = models.TextField()
    media = models.ImageField(upload_to='static/media/content', default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user')

    class Meta:
        verbose_name = "Post"

    def __str__(self) -> str:
        return self.topic


class CommentsModel(models.Model):

    """Model for commenting on posts"""

    timestamps = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(PostsModel, on_delete=models.CASCADE, related_name='post_for_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_for_comment')
    comment = models.TextField(default='')

    class Meta:
        verbose_name = "Comment"

    def __str__(self) -> str:
        return self.post.topic
