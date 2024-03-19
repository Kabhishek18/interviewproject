from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path('<int:feed_id>/comments/', views.FeedCommentsView.as_view(), name='feed_comments'),
    path('<int:feed_id>/comments/add/', views.AddCommentView.as_view(), name='add_comment'),
    path('<int:feed_id>/comments/report/', views.ReportCommentView.as_view(), name='report_comment'),
    # Add other URL patterns as needed
]
