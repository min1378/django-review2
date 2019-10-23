from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.conf import settings
# article.liked_users.all()
# user.liked_articles.all()
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # model에서 user를 가져올 때는 settings에서 직접 꺼내옴
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles', ) #user.liked_articles.all() => 유저가 좋아하는 모든 아티클 #article.liked_users.all() 아티클을 좋아하는 모든 유저
    class Meta:
        ordering = ('-pk', )


class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=100,
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
        )
    age = models.IntegerField(
        validators=[MinValueValidator(19, message='미성년자는 노노')]
    )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)