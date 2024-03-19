import uuid
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})

    def full_path(self):
        """Returns the full path of the category."""
        full_path = [self.title]
        parent_category = self.parent
        while parent_category is not None:
            full_path.append(parent_category.title)
            parent_category = parent_category.parent
        return ' -> '.join(full_path[::-1])
