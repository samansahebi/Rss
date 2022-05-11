from django.contrib import admin
from rss.models import Rss, News

# Register your models here.

admin.site.register(Rss)
admin.site.register(News)