from django.contrib import admin
from .models import Comments, News, AuthorsArticles
from .run import save_in_base, get_exchange_rates



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation_date_news', 'image')
    search_fields = ('title',)
    readonly_fields = ('title', 'text', 'creation_date_news', 'url', 'image')
    list_filter = ('creation_date_news',)
    fieldsets = (
        (None, {
            'fields': ('text', 'creation_date_news', 'url')
        }),
        ('Дополничельные данные', {
            'fields': ()}
         )
    )


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'news', 'creation_date', 'id')
    search_fields = ('user', 'news')
    readonly_fields = ('news', 'creation_date', 'user', 'comment_text')
    list_filter = ('creation_date',)

    fieldsets = (
        (None, {
            'fields': ('user', 'creation_date', 'comment_text')
        }),
        ('Дополничельные данные', {
            'fields': ('news',)}
         )
    )


@admin.register(AuthorsArticles)
class AuthorsArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date', 'moderation_done')
    search_fields = ('title',)
    readonly_fields = ('title', 'author', 'creation_date', 'text_article')
    list_filter = ('creation_date', 'moderation_done')
    fieldsets = (
        (None, {
            'fields': ('text_article', 'creation_date', 'moderation_done')
        }),
        ('Дополничельные данные', {
            'fields': ()}
         )
    )