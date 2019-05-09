from django.shortcuts import render

from django.core.cache import cache

# Create your views here.
from rest_framework.exceptions import APIException
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from Admin.authentication import AdminUserAuthentication
from Lost.settings import RESCUE_USER_TIMEOUT
from Rescue.models import RescueUser
from Rescue.permissions import AdminUserPermission
from Rescue.serializers import RescueUserSerializer
from utils.user_token_util import generate_rescue_token


class RescueUsersAPIView(ListCreateAPIView):

    queryset = RescueUser.objects.all()
    serializer_class =RescueUserSerializer
    authentication_classes = (AdminUserAuthentication, )
    permission_classes = (AdminUserPermission, )

    def post(self, request, *args, **kwargs):
        action = request.query_params.get("action")

        if action == "register":
            return self.create(request, *args, **kwargs)
        elif action == "login":
            return self.do_login(request, *args, **kwargs)
        else:
            raise APIException(detail="请提供正确动作")

    def do_login(self, request, *args, **kwargs):
        r_username = request.data.get("r_username")
        r_password = request.data.get("r_password")

        users = RescueUser.objects.filter(r_username=r_username)

        if not users.exists():
            raise APIException(detail="用户不存在")

        user = users.first()

        if not user.check_user_password(r_password):
            raise APIException(detail="密码错误")

        if user.is_delete:
            raise APIException(detail="用户已删除")

        token = generate_rescue_token()

        cache.set(token, user.id, timeout=RESCUE_USER_TIMEOUT)

        data = {
            "msg": "ok",
            "status": HTTP_200_OK,
            "token": token
        }
        return Response(data)