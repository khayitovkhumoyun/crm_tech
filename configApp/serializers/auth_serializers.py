from rest_framework import serializers
from ..models import *


# user madel ushun Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', "full_name", 'is_active', 'is_staff', 'is_admin')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',)


# passwordni uzgartirish uchun
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    re_new_password = serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):

        instance.password = validated_data.get('password', instance.password)

        if not validated_data['new_password']:
            raise serializers.ValidationError({'new_password': 'not found'})

        if not validated_data['old_password']:
            raise serializers.ValidationError({'old_password': 'not found'})

        if not instance.check_password(validated_data['old_password']):
            raise serializers.ValidationError({'old_password': 'wrong password'})

        if validated_data['new_password'] != validated_data['re_new_password']:
            raise serializers.ValidationError({'passwords': 'passwords do not match'})

        if validated_data['new_password'] == validated_data['re_new_password'] and instance.check_password(
                validated_data['old_password']):
            instance.set_password(validated_data['new_password'])
            instance.save()
            return instance

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 're_new_password']

#
# # tel raqamni qabulqilish uchun , bu serializerden kelgan data keshda saqlanadi
# class SMSSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#
#
# # tel raqam va otp ni qabul qiladi keshda saqlanadi
# class VerifySMSSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     verification_code = serializers.CharField()
