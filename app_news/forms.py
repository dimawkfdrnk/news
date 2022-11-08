from app_parser.models import Comments, News, AuthorsArticles
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comment_text']


class CreateAuthorsArticleForm(forms.ModelForm):

    class Meta:
        model = AuthorsArticles
        fields = ['title', 'text_article']