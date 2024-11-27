from django.db import models
from django.contrib.auth import get_user_model # User

User = get_user_model() # User


class Article(models.Model):
    # User
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default='')
    image = models.ImageField(blank=True, null=True)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

"""
jak nazvat třídu pro komentář k článku
jaké bude mít atributy
"""

class Comment(models.Model):
    # related_name definuje, pod jakým názvem budou dostupné komentáře z article
    # defautlně to je: comment_set
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        index = self.text.find(' ', 75)
        text = self.text[:index]
        return f'{self.autor}: {text}...'
