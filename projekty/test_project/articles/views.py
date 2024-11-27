from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from articles.models import Article
from articles.forms import CommentForm


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles2/article_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    # article = Article.objects.get(id=pk)
    form = CommentForm()
    context = {'article': article, 'form': form}
    return render(request, 'articles2/article_detail.html', context)

# /clanek/2/comment/
def create_comment(request, pk):
    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.article_id = pk
    comment.save()
    url = reverse('article_detail', kwargs={'pk': pk})
    return redirect(url)

# User

@login_required
def article_create(request):
    print(request.GET)
    if request.GET:
        article = Article.objects.create(
            title=request.GET['title'],
            content=request.GET['content'],
        )
        url = reverse('article_detail', kwargs={'pk': article.id})
        return redirect(url)

    return render(request, 'articles2/article_form.html')
