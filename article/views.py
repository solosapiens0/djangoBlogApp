from django.shortcuts import redirect, render, get_object_or_404, reverse

from .forms import ArticleForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles" : articles})
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles" : articles})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = { "articles" : articles }
    return render(request, "dashboard.html", context)

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "The article has been successfully saved...")
        return redirect("index")
        
    return render(request, "addarticle.html", {"form" : form})

def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)
    comments = article.comments.all()
    return render(request, "detail.html", {"article" : article, "comments" : comments})

@login_required(login_url = "user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "The article has been successfully updated...")
        return redirect("index")

    return render(request, "update.html", {"form" : form})

@login_required(login_url = "user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, "The article has been successfully deleted....")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article, id = id)
    if request.method == "POST":
        commentAuthor = request.POST.get("commentAuthor")
        commentContent = request.POST.get("commentContent")
        newComment = Comment(commentAuthor = commentAuthor, commentContent = commentContent)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail", kwargs = {"id" : id}))
    