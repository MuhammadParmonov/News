from test_app.models import Category, News

def category(request):
    categories = Category.objects.all()
    return {"kategoriyalar": categories}

def news(request):
    eng_news = News.objects.filter(holati=True).order_by("-koriwlar_soni")[0:5]
    return {"eng_kop": eng_news}