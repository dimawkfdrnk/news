from app_parser.models import Comments, News
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_text',)

