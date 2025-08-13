from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET', 'POST'])
def create_read_post(request):
    if request.method == 'GET':
        # GET으로 받았을 때는 모두 조회
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # POST로 받았을 때는 create
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def update_delete_post(request, post_pk):
    # PUT일 경우 수정
    
    try:
        post = Post.objects.get(id=post_pk)
        if request.method == 'PUT':
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            post = Post.objects.get(id=post_pk)
            post.delete()
            return Response({"message": "Post deleted successfully"},
                            status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response({"error": "The post matched with input key doesn't exist"})