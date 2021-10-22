from django.shortcuts import render
from articles.models import Article   


# Views
def home_page(request):
    articles = Article.objects.order_by("-date").all()
    articles = [format(data) for data in articles]

    data = {
        "articles": articles,
    }
    return render(request, "home.html", data)

# Helper funtions 

def format(data):
    return {
        "title": data.title,
        "date": data.date,
        "image": data.photo,
        "author": data.author,
        "summary": data.summary,
        "body": data.body
    }