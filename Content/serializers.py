from rest_framework import serializers
from .models import PostsModel


class PostsSerializer(serializers.ModelSerializer):

    """Serializer to get all posts"""

    class Meta:
        model = PostsModel
        fields = '__all__'