from django.shortcuts import redirect, get_object_or_404
from mall_backend.settings import get_secret
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
import requests

from mall.models import Account


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def kakao_login(req):
    if req.method == 'GET':
        CLIENT_ID = get_secret('KAKAO_REST_API_KEY')
        REDIRECT_URI = get_secret('KAKAO_REDIRECT_URI')
        url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}" \
            .format(CLIENT_ID, REDIRECT_URI)
        return redirect(url)
    else:
        uid = req.POST["uid"]
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, uid_kakao=uid)
        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            'user_id': user.pk,
            'email': user.email,
            'token': token.key,
        })


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def kakao_callback(req):
    tokenUrl = "https://kauth.kakao.com/oauth/token"
    res = {
        'grant_type': 'authorization_code',
        'client_id': get_secret('KAKAO_REST_API_KEY'),
        'redirect_url': get_secret('KAKAO_REDIRECT_URI'),
        'client_secret': get_secret('KAKAO_SECRET_KEY'),
        'code': req.query_params['code']
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }

    resp = requests.post(tokenUrl, data=res, headers=headers)

    authToken = resp.json()

    userUrl = "https://kapi.kakao.com/v2/user/me"
    HEADER = {
        "Authorization": "Bearer " + authToken['access_token'],
        'Content-type': "application/x-www-form-urlencoded;charset=utf-8"
    }
    resp = requests.get(userUrl, headers=HEADER)
    return Response({"uid": resp.json().get("id")})
