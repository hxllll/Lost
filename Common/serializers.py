from rest_framework import serializers

from Common.models import Loster

class LosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loster
        fields = ("l_name", "l_img", "l_age", "l_height", "l_feature", "l_f_feature", "l_isdna", "l_f_date", "l_f_site", "l_r_tel", "l_r_unit", "l_p_date", "l_r_info")