from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # models.ForeignKey(참조대상: 주로 class, on_delete=models.CASCADE)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)    # 제일 간단한 방법이나 클래스 정의 순서 따름
    # 아래의 방법은 app_name.class_name으로, 정의 순서와 상관 없이 다른 클래스와 관계 정의 가능
    # 대문자로 작성해도 migration에서는 소문자로 정정되는 것을 확인할 수 있음
    article = models.ForeignKey('articles.article', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

