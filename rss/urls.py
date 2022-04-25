from django.urls import path
from .views import NewsList, AddRss, GetRss

urlpatterns = [
    path('add-rss', AddRss.as_view()),
    path('get-rss', GetRss.as_view()),
    path('news', NewsList.as_view()),
]
