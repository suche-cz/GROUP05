# forms.py

from django import forms
from articles.models import Comment

CommentForm = forms.modelform_factory(
    Comment,
    fields=['autor', 'text'],
)
