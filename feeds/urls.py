from django.urls import path
from . import views

urlpatterns = [
    path('feeds/', views.FeedListCreateAPIView.as_view(), name='feed-list'),
    path('feeds/<uuid:pk>/', views.FeedRetrieveUpdateDestroyAPIView.as_view(), name='feed-detail'),
]