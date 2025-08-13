from rest_framework import serializers
from authors.models import Author

'''
    우리는 DB가 중요하므로 -> 예시는 계속 ModelSerializer 쓸 것
    model에 이미 author에 대한 정보 다 적어놨으므로
        그게 id, name ...
    그래서, 직렬화도 그 Model class Author에 있는 정보 그대로
    그냥 Serializer를 사용하면 모델에 대한 정보를 참고할 수 없음

class SomeSerializer(serializers.Serializer):
    # Serializer를 사용하면 여기에 데이터 형태를 정의할 수 있음
    title = serializers.CharField()
    content = serializers.CharField()
    opening_time = serializers.TimeField()

    # 위에서 정의한 필드를 최종적으로 Client한테 넘기는 걸 정의하는 게 Meta class
    class Meta:
        fiels = '__all__'

'''

class AuthorSerializer(serializers.ModelSerializer):
    # book_count 필드 정의하기
        # 정의하는 방법 2가지
        # 하나는 내가 직접 source 찾아서 때려박기 - 안 쓸 것
    # book_count = serializers.IntegerField(source='book_set.count', read_only=True)
    book_count = serializers.SerializerMethodField()
    def get_book_count(self, obj):
        # obj는 이 serializer를 호출한 객체: 여기서는 아마 author
        return obj.book_count
    
    class Meta:
        model = Author
        fields = '__all__'
        
class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'