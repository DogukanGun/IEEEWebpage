from django.shortcuts import render,get_object_or_404,redirect
from . import models
from .forms import ArticleForm
from .models import Article,Header
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
def news(request):
    return render(request,"Articles.html")
def article(request,id):
    article_ = get_object_or_404(Article,id = id)
    detail = article_.comments.all()
    return render(request,"Article.html",{"article":article_})
@user_passes_test(lambda u: u.is_superuser)
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("Article:dashboard")
    return render(request,"addarticle.html",{"form":form})
@user_passes_test(lambda u: u.is_superuser)
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})
@user_passes_test(lambda u: u.is_superuser)
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("article:dashboard")
# Create your views here.
