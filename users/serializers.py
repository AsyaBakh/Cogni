from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'password', 'name', 'description', 'email', 'image', 'type_mbti', 'id_role', 'id_MBTI_type')
    extra_kwargs = {'password': {'write_only': True}, 'image': {'required': False}}

  def create(self, validated_data):
    password = validated_data.pop('password')
    user = CustomUser(**validated_data)
    user.set_password(password)
    user.save()
    return user
