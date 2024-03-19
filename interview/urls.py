from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include('feeds.urls')),
    path('v1/',include('subjects.urls')),
    path('v1/',include('comments.urls')),
]
