from rest_framework import serializers

from api.models import Salary


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"
