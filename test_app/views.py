from django.shortcuts import render, redirect
from django.urls.base import reverse

from .models import News, Category
from .forms import NewsForm, CategoryForm

def main_page(request):
    search = request.GET.get("soz", None)
    if request.method == "GET" and search != None:
        news = News.objects.filter(nomi__contains=search).order_by("-id")
        context = {
            "yangiliklar": news,
        }
        return render(request, "index.html", context)
    else:
        news = News.objects.all().order_by("-id")
        context = {
            "yangiliklar": news,
        }
        return render(request, "index.html", context)

def category_page(request, cat_id):
    news = News.objects.filter(category=cat_id)
    context = {
        "yangiliklar": news
    }
    return render(request, "index.html", context)

def batafsil_page(request, id):
    news = News.objects.get(id=id)
    news.koriwlar_soni+=1
    news.save()
    context = {
        "yangilik": news
    }
    return render(request, "batafsil.html", context)

def add_news(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("home-page"))

    context = {
        "form": form
    }
    return render(request, "add_news.html", context)

def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home-page"))
    context = {
        "form": form
    }
    return render(request, "add_category.html", context)

def admin_page(request):
    news = News.objects.filter()
    context = {
        "yangiliklar": news
    }
    return render(request, 'admin_panel.html', context)

def del_news(request, news_id):
    news = News.objects.get(id=news_id)
    if news:
        news.delete()
    return redirect(reverse("admin-page"))

def yangilik_holati(request, news_id):
    news = News.objects.get(id=news_id)
    if news and news.holati==True:
        news.holati = False
        news.save()
    elif news and news.holati==False:
        news.holati = True
        news.save()
    return redirect(reverse("admin-page"))