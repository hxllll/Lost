from django.db import models


# Create your models here.

class Loster(models.Model):
    l_name = models.CharField(max_length=64)
    l_img = models.CharField(max_length=256)
    l_age = models.IntegerField(default=0)
    l_height = models.IntegerField(default=160)
    l_feature = models.CharField(max_length=256)
    l_f_feature = models.CharField(max_length=256)
    l_isdna = models.BooleanField(default=False)
    l_f_date = models.DateTimeField(auto_now_add=True)
    l_f_site = models.CharField(max_length=256)
    l_r_tel = models.CharField(max_length=32)
    l_r_unit = models.CharField(max_length=256)
    l_p_date = models.DateTimeField(auto_now_add=True)
    l_r_info = models.CharField(max_length=256)
