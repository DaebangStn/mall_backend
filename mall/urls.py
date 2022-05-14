from django.urls import path, include
from mall.views import kakao_callback, google_callback, google_login, \
    kakao_login, naver_login, naver_callback, account_list, account_detail, \
    account_oauth_register, CategoryViewSet, ItemViewSet, OrderViewSet, \
    ReviewViewSet, CategoryRootView, CategorySubView
from rest_framework.authtoken import views as auth_view
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('items', ItemViewSet, basename='item')
router.register('orders', OrderViewSet, basename='order')
router.register('reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('account/', account_list),
    path('account/<str:username>', account_detail),
    path('auth/login/', auth_view.obtain_auth_token),
    path('auth/google/login/', google_login),
    path('auth/google/login/callback/', google_callback),
    path('auth/kakao/login/', kakao_login),
    path('auth/kakao/login/callback/', kakao_callback),
    path('auth/naver/login/', naver_login),
    path('auth/naver/login/callback/', naver_callback),
    path('auth/register/<str:username>', account_oauth_register),
]


urlpatterns += [
    path('categories/root/', CategoryRootView.as_view()),
    path('categories/sub/<str:category>', CategorySubView.as_view()),

    # router url should come later. because it takes all
    path('', include(router.urls)),
]
