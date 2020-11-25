from rest_framework import serializers
from .models import NewsContent


class NewsContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'headline', 'body')
        model = NewsContent