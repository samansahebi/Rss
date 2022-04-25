import feedparser
from celery import shared_task
from .models import Rss, News


@shared_task
def gather_rss():
    rss = Rss.objects.all()
    for r in rss:
        data = feedparser.parse(r.url)
        if not News.objects.filter(text=data['feed']).exists():
            News.objects.create(rss=r, text=data['feed']).save()


