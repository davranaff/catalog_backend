from rest_framework import serializers

from app.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Menu
        fields = '__all__'
