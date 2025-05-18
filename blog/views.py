from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseForbidden



from rest_framework.response import Response
from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk']).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    작성자만 수정/삭제 가능
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS는 허용
            return True
        return obj.author == request.user  # 작성자인 경우에만 PUT/DELETE 허용


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # 👈 여기에 추가
    filter_backends = [filters.SearchFilter]  # 👈 검색 활성화
    search_fields = ['title', 'content']      # 👈 이 필드에서 검색

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@login_required
def post_new_html(request):
    return render(request, 'blog/post_new.html')

# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)  # 👈 저장을 잠깐 멈춤
#             post.author = request.user      # 👈 현재 로그인한 사용자 할당
#             post.save()                     # 👈 그 다음 저장
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_new.html', {'form': form})

def post_list_html(request):
    return render(request, 'blog/post_list.html')

# def post_list(request):
#     query = request.GET.get('q')  # 검색어 가져오기
#     if query:
#         posts = Post.objects.filter(
#                 Q(title__icontains=query) | Q(content__icontains=query)
#                 ).order_by('-created_at')
#     else:
#         posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/post_list.html', {'posts': posts, 'query': query})

def post_detail_html(request, pk):
    return render(request, 'blog/post_detail.html', {'post_id': pk})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('post_list')

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit_html(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("접근 권한이 없습니다.")
    return render(request, 'blog/post_edit.html', {'post_id': pk})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 바로 로그인
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})