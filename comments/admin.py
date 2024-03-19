from django.contrib import admin
from django import forms
from django.db import models
from django.utils.html import format_html
from .models import Comment, EmojiReaction, CommentReport

# admin.site.register(Comment)
admin.site.register(EmojiReaction)
admin.site.register(CommentReport)

# Optionally, you can customize the admin view for Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'feed', 'is_spam']
    list_filter = ['is_spam']
    search_fields = ['text', 'user__username']