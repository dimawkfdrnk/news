from django.contrib import admin
from django.contrib import admin
from app_parser.models import Comments

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'news', 'creation_date')
    search_fields = ('user', 'comment_text')

