from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import User


class PostsModel(models.Model):

    """Post storage model"""

    STATUS_POST = [
        ('pending', 'pending'),
        ('active', 'active')
    ]

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    topic = models.CharField(max_length=255, default='')

    base = models.TextField(default='', blank=True)
    gameplay = models.TextField(default='', blank=True)
    growth = models.TextField(default='', blank=True)
    latest_update = models.TextField(default='', blank=True)


    status = models.CharField(max_length=255, choices=STATUS_POST, default='pending')
    media_main_post = models.ImageField(upload_to='content', default='', blank=True)
    count_views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user', blank=True)

    media_sidebar = models.ImageField(upload_to='content', default='', blank=True)
    developers = models.TextField(default='' , blank=True)
    publishers = models.TextField(default='', blank=True)
    genres = models.CharField(max_length=255, default='', blank=True)
    release_dates = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    game_modes = models.CharField(max_length=255, default='', blank=True)
    platforms = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        verbose_name = "Post"

    def __str__(self) -> str:
        return self.topic

    def search_post(self):
        return 


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
    footer_text = models.TextField(default='')

    def __str__(self) -> str:
        return self.welcome_phrase

    def save(self, *args, **kwargs):
        if not self.pk and Settings.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationErr('There is can be only one JuicerBaseSettings instance')
        return super(Settings, self).save(*args, **kwargs)
