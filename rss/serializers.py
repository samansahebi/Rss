from rest_framework.serializers import ModelSerializer
from .models import Rss, News


class RssSerializer(ModelSerializer):
    class Meta:
        model = Rss
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
