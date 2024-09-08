from .models import Post 
from rest_framework import viewsets
from .serializers import PostSerializer
# Create your views here.


"""
import viewsets -> 여러 http메소드(get,post,delete,put)를 처리해줌ㅡ 이때 코드 중복 줄여주는 클래스 기반 뷰
class PostViewSet(viewsets.ModelViewSet):-> 새로운 postviewsSet을 만듦
queryset = Post.objects.all() -> 기본 쿼리셋을 정의, API가 모든 게시글에 대해 CRUD가 가능함
serializer_class = PostSerializer -> 사용할 시리얼라이저 클래스를 지정함

GET /posts/: 모든 게시글을 조회합니다.
POST /posts/: 새로운 게시글을 생성합니다.
GET /posts/{id}/: 특정 ID의 게시글을 조회합니다.
PUT /posts/{id}/: 특정 ID의 게시글을 수정합니다.
DELETE /posts/{id}/: 특정 ID의 게시글을 삭제합니다.
"""

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
