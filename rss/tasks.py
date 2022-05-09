import feedparser
from celery import shared_task
from .models import Rss, News


@shared_task
def gather_rss():
    rss = Rss.objects.all()
    for r in rss:
        data = feedparser.parse(r.url)
        for entry in data.entries:
            if not News.objects.filter(text=entry['title']).exists():
                News.objects.create(rss=r, text=entry['title']).save()


