from .models import *
from rest_framework.serializers import ModelSerializer

class AutoBranchSerializer(ModelSerializer):
    class Meta:
        model = AutoBranch
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AutomobileSerializer(ModelSerializer):
    class Meta:
        model = Automobile
        fields = '__all__'