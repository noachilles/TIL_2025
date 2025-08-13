# articles/serializers.py

from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('created_at', 'updated_at',)


# 게시글 조회 할 때 해당 게시글의 댓글도 함께 조회
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)   # 댓글의 id와 content만 보여준다.

    # read_only=True 옵션을 통해 해당 필드를 읽기 전용으로 설정할 수 있다.
    comment_set = CommentDetailSerializer(many=True, read_only=True) # related_name을 통해 역참조
    # 댓글 갯수 표시
    
    # method로 정의된 형태로 보여줄 것
    num_of_comments = serializers.SerializerMethodField()

    # get이라는 이름을 붙여야 정상작동됨
    def get_num_of_comments(self, obj):
        # 여기서 obj는 Serializer가 처리하는 Article 인스턴스
        # view에서 annotate 한 필드를 그대로 사용 가능 - fields 내용에 추가되어서 나오는 것을 확인할 수 있음
        return obj.num_of_comments

    class Meta:
        model = Article
        fields = '__all__'
        # # fields = ('id', 'title',)
        # exclude = ('created_at', 'updated_at',)



# 댓글 조회 시 게시글 정보도 함께 조회
class CommentSerializer(serializers.ModelSerializer):
    # class ArticleForCommentSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Article
    #         fields = ('id', 'title', )

    # article = ArticleForCommentSerializer(read_only=True)

    # 이 serializer가 호출될 때, article을 정의

    class Meta:
        model = Comment
        ''' 
            게시글의 정보도 함께 보고싶음 - 댓글을 '생성'할 때는 article 정보를 서버가 처리
            단, 댓글을 조회할 때는 article 정보도 포함해 반환
        '''
        

        # tuple에 요소 1개일 때 trailing comma 찍어야 함.
        fields = '__all__'
        # all로 할 때만 아래 article 결과가 출력됨
        read_only_fields = ('article', )

