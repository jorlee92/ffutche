from home.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class TuitionFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition_Fees
        fields = '__all__'

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = '__all__'