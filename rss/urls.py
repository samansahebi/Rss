from django.urls import path
from .views import NewsList

urlpatterns = [
    path('add-rss', NewsList.as_view()),
    path('news', NewsList.as_view()),
]
