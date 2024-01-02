from rest_framework import serializers
from cc_app.models import OutputLocationSetter, VideoUpload
from django.conf import settings


class OutputLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputLocationSetter
        fields = "__all__"
