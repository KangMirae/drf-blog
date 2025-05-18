from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views
from .views import PostViewSet
from .views import signup
from .views import post_new_html
from .views import post_list_html
from .views import post_detail_html
from .views import post_edit_html, PostViewSet, CommentViewSet


# router = DefaultRouter()
# router.register('api/posts', PostViewSet)

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

post_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
post_router.register('comments', CommentViewSet, basename='post-comments')



urlpatterns = [
    path('accounts/signup/', signup, name='signup'),  # ✅ 이 줄!
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', post_list_html, name='post_list_html'),  # 🟢 추가!
    path('post/<int:pk>/', post_detail_html, name='post_detail_html'),  # ✅ 추가
    path('post/<int:pk>/edit/', post_edit_html, name='post_edit_html'),  # ✅ 추가!
    path('api/', include(router.urls)),
    path('api/', include(post_router.urls)),
    path('post/new/', post_new_html, name='post_new_html'),  # 👈 이거 추가!
    path('', include(router.urls)),  # 👈 자동으로 CRUD URL이 생김
]
