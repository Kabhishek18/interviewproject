import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from feeds.models import Feed

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    EMOJI_CHOICES = (
        ('👍', 'Like'),
        ('👎', 'Dislike'),
        ('❤️', 'Love'),
        ('😂', 'Laugh'),
        ('😮', 'Surprised'),
        ('😢', 'Sad'),
        ('😡', 'Angry'),
    )
    emoji_reactions = models.ManyToManyField(User, through='EmojiReaction', related_name='emoji_reactions', blank=True)
    is_spam = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.user:
            return f'{self.created_at} Comment by {self.user.username} on {self.feed.question}'
        else:
            return f'Anonymous Comment on {self.feed.question}'

class EmojiReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=2, choices=Comment.EMOJI_CHOICES)

    class Meta:
        unique_together = ['user', 'comment', 'emoji']

    def __str__(self):
        return f'{self.user.username} reacted with {self.get_emoji_display()} to {self.comment}'

class CommentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} reported {self.comment} for {self.reason}'

@receiver(post_save, sender=CommentReport)
def update_comment_spam_status(sender, instance, created, **kwargs):
    if created:
        report_count = CommentReport.objects.filter(comment=instance.comment).count()
        if report_count >= 20:
            instance.comment.is_spam = True
            instance.comment.save()
