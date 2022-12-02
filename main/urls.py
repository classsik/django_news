from django.urls import path

from .views import home, add_news

urlpatterns = [
    path('', home),
    path('news/add/', add_news)
]
