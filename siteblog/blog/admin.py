from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    form = PostAdminForm
    #save_as = True #сохранить как новый объект
    list_display = ('id', 'title', 'author', 'created_at', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'author', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

admin.site.site_title = 'Управление блогом'
admin.site.site_header = 'Управление блогом'
