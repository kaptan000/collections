from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    # employee_id = serializers.IntegerField(read_only = True)
    # first_name = serializers.CharField(max_length = 50)
    # last_name = serializers.CharField(max_length = 50)
    # department = serializers.CharField(max_length=40)
    # total_experience = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = "__all__"