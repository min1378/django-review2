from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from IPython import embed
from django.views.decorators.http import require_GET, require_POST
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)





def create(request):
    if request.method == 'POST':
        #Article을 생성해달라고 하는 요청
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: #GET
        # Article을 생성하기 위한 페이지를 달라고 하는 요청
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)



def detail(request, article_pk):
    #사용자가 적어보낸 article_pk를 통해 세부 페이지를 보여준다.
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    form = CommentForm()
    context = {
        'article' : article,
        'comments' : comments,
        'form' : form,

    }
    return render(request, 'articles/detail.html', context)





def update(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
        
    if request.method == 'GET':
        form = ArticleForm(instance=article)
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html', context)
    


@require_POST
def delete(request, article_pk):
    # article_pk에 맞는 article을 꺼낸다.
    # 삭제한다.
    #if request.method == 'POST':
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()    
    return redirect('articles:index')

@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # push 전의 상태를 담아둠
        comment.article = article  # 빠진 필드 채워넣기
        comment.save()
    return redirect('articles:detail', article_pk)
    # article_pk에 해당하는 article에 새로운 comment 생성
    # 생성한 다음 article detail page 로 redirect

def comment_delete(request, comment_pk, article_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)