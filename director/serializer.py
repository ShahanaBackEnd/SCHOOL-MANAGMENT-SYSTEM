from rest_framework import serializers
from .models import Year_Level,classroom_type

class year_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year_Level
        fields = "__all__"

class classroom_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom_type
        fields = "__all__"