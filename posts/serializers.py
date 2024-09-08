from rest_framework import serializers
from .models import Post

"""
serializers.ModelSerializer -> 모델필드에 해당하는 시리얼라이저 필드를 자동으로 생성
class Meta -> Meta클래스는 시리얼라이저의 메타데이터를 정의하는 내부 클래스
model = Post -> 모델은 우리가 만든 post사용
fileds = '__all__' => 모델의 모든 필드를 시리얼라이즈에 연결
"""
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'