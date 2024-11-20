from django.shortcuts import render, get_object_or_404
from articles.models import Article

def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles2/article_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    # article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'articles2/article_detail.html', context)