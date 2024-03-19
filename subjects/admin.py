from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','parent', 'created_on', 'modified_on')
    search_fields = ('title', 'slug','parent','id')
