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
def google_login(req):
    if req.method == 'GET':
        scope = "https://www.googleapis.com/auth/userinfo.profile"
        CLIENT_ID = get_secret("GOOGLE_CLIENT_ID")
        REDIRECT_URI = get_secret("GOOGLE_REDIRECT_URI")
        url = "https://accounts.google.com/o/oauth2/v2/auth?client_id={}&".format(CLIENT_ID) + \
            "response_type=code&redirect_uri={0}&scope={1}".format(REDIRECT_URI, scope)
        return redirect(url)
    else:
        uid = req.POST["uid"]
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, uid_google=uid)
        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            'user_id': user.pk,
            'email': user.email,
            'token': token.key,
        })


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly, ])
def google_callback(request):
    CLIENT_ID = get_secret("GOOGLE_CLIENT_ID")
    SECRET = get_secret("GOOGLE_SECRET")
    REDIRECT_URI = get_secret("GOOGLE_REDIRECT_URI")
    code = request.GET.get('code')

    url = "https://oauth2.googleapis.com/token?client_id={0}&client_secret={1}&" \
        .format(CLIENT_ID, SECRET) + \
          "code={0}&grant_type=authorization_code&redirect_uri={1}" \
        .format(code, REDIRECT_URI)

    resp = requests.post(url)
    authToken = resp.json()

    access_token = authToken.get('access_token')

    resp = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")

    return Response({"uid": resp.json().get("user_id")})
