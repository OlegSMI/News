from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    """comment"""
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'views', 'get_photo' )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    fields = ( 'title', 'content','created_at', 'updated_at', 'is_published', 'category', 'views', 'get_photo')
    readonly_fields = ('created_at', 'updated_at', 'views', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'nou nou nou'

    get_photo.short_description = 'Миниатюра'


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CatAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостямими'