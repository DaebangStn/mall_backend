from django.http import HttpResponse
from .kakao_oauth import kakao_callback, kakao_login
from .google_oauth import google_callback, google_login
from .naver_oauth import naver_callback, naver_login
from .account_viewSet import account_list, account_detail, account_oauth_register

from .category_viewSet import CategoryViewSet, CategoryRootView, CategorySubView
from .item_viewSet import ItemViewSet
from .order_viewSet import OrderViewSet
from .review_ViewSet import ReviewViewSet

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny, ])
def index(req):
    print(req.auth)
    return HttpResponse('hi')
