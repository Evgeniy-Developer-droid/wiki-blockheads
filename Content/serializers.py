from rest_framework import serializers
from .models import PostsModel


class PostsSerializer(serializers.ModelSerializer):

    """Serializer to get all posts"""

    class Meta:
        model = PostsModel
        fields = '__all__'


class SinglePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostsModel
        fields = '__all__'

    def to_representation(self, instance):
        return {
            "post_info": [
                {
                    "created": instance.created,
                    "topic": instance.topic,
                    "base": instance.base,
                    "gameplay": instance.gameplay,
                    "growth": instance.growth,
                    "latest_update": instance.latest_update,
                    "media_main_post": instance.media_main_post.url,
                    "count_views": instance.count_views,
                    "user": instance.user.username
                },
            ],
            "additional_info": [
                {
                    "media_sidebar": instance.media_sidebar.url,
                    "developers": instance.developers,
                    "publishers": instance.publishers,
                    "genres": instance.genres,
                    "release_dates": instance.release_dates,
                    "game_modes": instance.game_modes,
                    "platforms": instance.platforms
                }
            ]
        }
