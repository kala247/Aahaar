from rest_framework import serializers
from bhojan.models import Partymenu


class BhojanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partymenu
        fields = "__all__"
        read_only_fields = ['img']

class BhojanpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partymenu
        fields =['img']

