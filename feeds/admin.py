from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from .models import Feed

class FeedAdminForm(forms.ModelForm):
    use_ckeditor = forms.BooleanField(required=False, label='Use Wswyg for Question')

    class Meta:
        model = Feed
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
            'answer': CKEditorWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].widget = forms.Textarea() 

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('use_ckeditor'):
            self.fields['question'].widget = CKEditorWidget()
        return cleaned_data

class FeedAdmin(admin.ModelAdmin):
    form = FeedAdminForm
    list_display = ('question', 'user', 'created_on', 'modified_on', 'status')
    list_filter = ('status',)
    search_fields = ('question', 'answer')
    readonly_fields = ('created_on', 'modified_on')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user 
        return form

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()


admin.site.register(Feed, FeedAdmin)
