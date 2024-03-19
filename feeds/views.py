from rest_framework import generics
from django.shortcuts import render
from .models import Feed
from comments.models import Comment, EmojiReaction, CommentReport
from .serializers import FeedSerializer
from django.views import View


class FeedListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedView(View):

    @classmethod
    def get(cls,request):
        feeds_with_comments = []
        feeds = Feed.objects.all().order_by("ordinal")
        for feed in feeds:
            comments = Comment.objects.filter(feed=feed, parent_comment__isnull=True)  # Fetching only top-level comments
            comments_with_replies = []
            for comment in comments:
                print("$%$%"*100, comment)
                replies = comment.replies.all() 
                comments_with_replies.append({'comment': comment, 'replies': replies})
            feeds_with_comments.append({'feed': feed, 'comments_with_replies': comments_with_replies})
                
        return render(request, 'feed_details.html', {'feeds_with_comments': feeds_with_comments})
        

    