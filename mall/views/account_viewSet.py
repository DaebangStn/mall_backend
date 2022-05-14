from mall.models import Account
from django.shortcuts import get_object_or_404
from mall.serializers import AccountSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def list(self, req):
        queryset = Account.objects.all()
        serializer = AccountSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, req, username=None):
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, username=username)
        serializer = AccountSerializers(user)
        return Response(serializer.data)

    def register_oauth(self, req, username=None):
        queryset = Account.objects.all()
        user = get_object_or_404(queryset, username=username)
        provider = req.POST["provider"]
        uid = req.POST["uid"]

        serializer = AccountSerializers(user)

        if provider == "google":
            serializer = AccountSerializers(user, data={"uid_google": uid}, partial=True)
        elif provider == "naver":
            serializer = AccountSerializers(user, data={"uid_naver": uid}, partial=True)
        elif provider == "kakao":
            serializer = AccountSerializers(user, data={"uid_kakao": uid}, partial=True)

        serializer.is_valid()
        serializer.save()
        return Response("Succeed")


account_list = AccountViewSet.as_view({
    'get': 'list',
})

account_detail = AccountViewSet.as_view({
    'get': 'retrieve',
})

account_oauth_register = AccountViewSet.as_view({
    'post': 'register_oauth',
})
