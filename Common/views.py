from django.shortcuts import render

# Create your views here

from rest_framework.generics import ListCreateAPIView

from Admin.authentication import AdminUserAuthentication
from Admin.permission import SuperAdminUserPermission
from Common.models import Loster
from Common.serializers import LosterSerializer


class LosterAPIView(ListCreateAPIView):

    queryset = Loster.objects.all()
    serializer_class = LosterSerializer
    # authentication_classes = (AdminUserAuthentication,)
    # permission_classes = (SuperAdminUserPermission,)