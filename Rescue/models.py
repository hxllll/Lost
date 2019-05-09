from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.

RESCUE_REGISTER = 0
RESCUE_ACTIVE = 1
RESCUE_CAN_CREATE = 2
RESCUE_CAN_DELETE = 4


class RescueUser(models.Model):
    r_username = models.CharField(max_length=32, unique=True)
    r_password = models.CharField(max_length=256)
    r_tel = models.CharField(max_length=32)
    r_site = models.CharField(max_length=64)

    is_delete = models.BooleanField(default=False)
    r_permission = models.IntegerField(default=RESCUE_REGISTER)

    def check_permission(self, permission):
        return self.r_permission & permission == permission

    def set_password(self, password):
        self.r_password = make_password(password)

    def check_user_password(self, password):
        return check_password(password, self.r_password)
