from django.shortcuts import render

from .forms import NewsAddForm

news = [
    {
        'id': 0,
        'title': 'News Title',
        'text': "News Text",
        "image": ''
    },
    {
        'id': 1,
        'title': 'News Title',
        'text': "News Text",
        "image": ''
    },
    {
        'id': 2,
        'title': 'News Title',
        'text': "News Text",
        "image": ''
    }
]


def home(request):
    return render(request, 'main/news.html', {"news": news})


def add_news(request):
    form = NewsAddForm()
    return render(request, 'main/form.html', {'form': form})
