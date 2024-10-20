from rest_framework import serializers
from .models import CustomUser


class LoginSerializer(serializers.Serializer):
 username = serializers.CharField()
 password = serializers.CharField()

 def validate(self, data):
  username = data.get('username')
  password = data.get('password')

  if not username and not password:
   raise serializers.ValidationError("Заполните поля 'username' и 'password'")

  user = CustomUser.objects.filter(username=username).first()
  if user is None:
   raise serializers.ValidationError("Пользователь не найден")

  if not user.check_password(password):
   raise serializers.ValidationError("Неверный пароль")

  return data


class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = CustomUser
  fields = ('username', 'email', 'password', 'type_mbti')
  extra_kwargs = {'password': {'write_only': True}}

 def create(self, validated_data):
  password = validated_data.pop('password')
  user = CustomUser(**validated_data)
  user.set_password(password)
  user.save()
  return user
