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
def naver_login(req):
    if req.method == 'GET':
        CLIENT_ID = get_secret('NAVER_CLIENT_ID')
        REDIRECT_URI = get_secret('NAVER_REDIRECT_URI')
        url = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={0}&redirect_uri={1}" \
            .format(CLIENT_ID, REDIRECT_URI)
        return redirect(url)
    else:
        uid = req.POST["uid"]
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, uid_naver=uid)
        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            'user_id': user.pk,
            'email': user.email,
            'token': token.key,
        })


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def naver_callback(req):
    tokenUrl = "https://nid.naver.com/oauth2.0/token"
    res = {
        'grant_type': 'authorization_code',
        'client_id': get_secret('NAVER_CLIENT_ID'),
        'redirect_url': get_secret('NAVER_REDIRECT_URI'),
        'client_secret': get_secret('NAVER_SECRET'),
        'code': req.query_params['code']
    }

    resp = requests.post(tokenUrl, data=res)

    authToken = resp.json()

    userUrl = "https://openapi.naver.com/v1/nid/me"
    HEADER = {
        "Authorization": "Bearer " + authToken['access_token'],
    }
    resp = requests.get(userUrl, headers=HEADER)
    uid = resp.json().get("response").get("id")
    return Response({"uid": uid})
