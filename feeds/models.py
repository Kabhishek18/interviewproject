import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from subjects.models import Category as SubjectCategory  

class Feed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    question = models.TextField()
    answer = models.TextField()
    slug = AutoSlugField(populate_from='question', unique=True, editable=False)
    categories = models.ManyToManyField(SubjectCategory, related_name='feeds')
    level = models.IntegerField(choices=((1, '1 Star'), (2, '2 Star'), (3, '3 Star'),(4, '4 Star'),(5, '5 Star')), default=1)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question[:20]}..."

    class Meta:
        unique_together = ('slug', 'question',)
        verbose_name_plural = "Feeds"
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('feed_detail', kwargs={'pk': self.pk})
