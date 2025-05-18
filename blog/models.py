from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}의 댓글: {self.content[:20]}'

class Post(models.Model):
    title = models.CharField(max_length=200)            # 글 제목
    content = models.TextField()                        # 글 본문
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간 자동 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자 필드 추가

    def __str__(self):
        return self.title
