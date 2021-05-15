from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='Post')
v1_router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                   basename='Comment')
v1_router.register(r'follow', FollowViewSet, basename='Follow')
v1_router.register(r'group', GroupViewSet, basename='Group')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(v1_router.urls)),
]
