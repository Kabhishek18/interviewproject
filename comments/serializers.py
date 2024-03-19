from rest_framework import serializers
from models import Comment, EmojiReaction, CommentReport
from django.db import models

class EmojiReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmojiReaction
        fields = '__all__'

class CommentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReport
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    emoji_reactions = EmojiReactionSerializer(many=True, read_only=True)
    reports = CommentReportSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
