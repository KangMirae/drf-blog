from django.utils.timesince import timesince

from rest_framework import serializers

from datetime import datetime

from .models import Post
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_display = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'created_display']
        read_only_fields = ['id', 'author', 'created_at', 'post']
    
    def get_created_display(self, obj):
        return timesince(obj.created_at) + ' 전'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comment_count = serializers.SerializerMethodField()  # 👈 추가!

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()
