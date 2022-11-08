from django.contrib import admin
from app_parser.models import Comments, News
from app_parser.run import save_in_base, get_exchange_rates


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation_date_news', 'image')
    search_fields = ('title',)
    readonly_fields = ('title', 'text', 'creation_date_news', 'url', 'image')
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'creation_date_news', 'url')
        }),
        ('Дополничельные данные', {
            'fields': ()}
         )
    )



@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'news', 'creation_date')
    search_fields = ('user', 'news')
    readonly_fields = ('news','creation_date', 'user', 'comment_text')

    fieldsets = (
        (None, {
            'fields': ('user', 'creation_date', 'comment_text')
        }),
        ('Дополничельные данные', {
            'fields': ('news',)}
         )
    )

