from rest_framework import serializers
from .models import DonorModel,BloodInventoryModel,BloodRequestModel
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken



class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}



class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorModel
        fields = "__all__"


class BloodInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodInventoryModel
        fields = "__all__"


class BloodRequestSerializer(serializers.ModelSerializer):
    class meta:
        model= BloodRequestModel
        fields = "__all__"