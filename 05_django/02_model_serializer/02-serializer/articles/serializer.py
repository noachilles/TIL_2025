from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    # 직렬화
    class Meta:
        # 모델에 대한 정보를 토대로
        model = Article
        # field = '__all__'
        fields = ('id', 'title',)   # 특정 요소만

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'