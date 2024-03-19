from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
from .models import Comment, Feed, CommentReport

class FeedCommentsView(ListView):
    template_name = 'feeds/feed_comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        feed_id = self.kwargs['feed_id']
        feed = get_object_or_404(Feed, pk=feed_id)
        return Comment.objects.filter(feed=feed)

class AddCommentView(View):
    def post(self, request, feed_id):
        feed = get_object_or_404(Feed, pk=feed_id)
        user = request.user if request.user.is_authenticated else None
        text = request.POST.get('text')
        if text:
            Comment.objects.create(feed=feed, user=user, text=text)
        return redirect('feeds:feed_comments', feed_id=feed_id)

class ReportCommentView(View):
    def post(self, request, feed_id):
        comment_id = request.POST.get('comment_id')
        reason = request.POST.get('reason')
        comment = get_object_or_404(Comment, pk=comment_id)
        user = request.user
        CommentReport.objects.create(comment=comment, user=user, reason=reason)
        return redirect('feeds:feed_comments', feed_id=feed_id)
