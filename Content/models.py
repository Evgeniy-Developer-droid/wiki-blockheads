from django.db import models
from django.contrib.auth.models import User


class PostsModel(models.Model):

    """Post storage model"""

    STATUS_POST = [
        ('pending', 'pending'),
        ('active', 'active')
    ]

    update = models.DateTimeField(null=True, blank=True)

    timestamps = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255, default='')
    message = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_POST, default='pending')
    media_main_post = models.ImageField(upload_to='content', default='', blank=True)
    count_views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user')

    media_sidebar = models.ImageField(upload_to='content', default='', blank=True)
    developers = models.TextField(default='' , blank=True)
    publishers = models.TextField(default='', blank=True)
    genres = models.CharField(max_length=255, default='')
    release_dates = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    game_modes = models.CharField(max_length=255, default='', blank=True)
    platforms = models.CharField(max_length=255, default='', blank=True)

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


class Settings(models.Model):

    welcome_phrase = models.CharField(max_length=255)
    description_site = models.TextField(default='')

    single_page_title = models.CharField(max_length=255, default='')

    footer_text = models.TextField(default='')

    def __str__(self) -> str:
        return self.welcome_phrase
