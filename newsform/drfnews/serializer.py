from rest_framework import serializers
from website.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'city', 'business', 'sport',
                  'health', 'politika', 'news_photo', 'sport_photo', "politika_photo", "news_title", "sport_title")
