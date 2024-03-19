from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<uuid:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]
