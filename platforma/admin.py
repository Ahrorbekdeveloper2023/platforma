from django.contrib import admin

### platforma.models
from .models import User, Kurs, Dars, Video, Comment, Like

### register

class DarsInline(admin.StackedInline):
    model = Dars
    extra = 0

class VideoInline(admin.StackedInline):
    model = Video
    extra = 0

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class LikeInline(admin.StackedInline):
    model = Like
    extra = 0

@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'start_date', 'author',)
    list_display_links = ('name',)
    list_editable = ('author',)
    list_filter = ('name', 'price',)
    search_fields = ('name', 'price', 'author',)
    inlines = [
        DarsInline
    ]


@admin.register(Dars)
class DarsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'kurs', 'title', 'text', 'author',)
    list_display_links = ('title',)
    list_editable = ('kurs', 'author',)
    list_filter = ('title', 'kurs',)
    search_fields = ('title', 'text',)
    inlines = [
        VideoInline
    ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'dars', 'video', 'author',)
    list_display_links = ('pk',)
    list_editable = ('dars', 'author',)
    list_filter = ('video',)
    search_fields = ('title', 'text', 'author',)
    inlines = [
        CommentInline,
        LikeInline,
    ]



admin.site.register([User])
