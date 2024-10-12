from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import CustomUser, Role, MBTI_type

# Регистрация нового пользователя
@api_view(['POST'])
def register(request):
  if request.method == 'POST':
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()

      # Добавление данных профиля пользователя в CustomUser
      user.name = request.data.get('name')
      user.description = request.data.get('description')
      user.type_mbti = request.data.get('type_mbti')

      # Получение роли и типа MBTI
      role = Role.objects.get(pk=request.data.get('id_role'))
      mbti_type = MBTI_type.objects.get(pk=request.data.get('id_MBTI_type'))
      user.id_role = role
      user.id_MBTI_type = mbti_type

      # Обработка изображения
      if 'image' in request.FILES:
        image = request.FILES['image']
        user.image = image
      user.save()

      # Возвращаем данные нового пользователя в JSON
      return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Вход в систему
class login(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'token': token.key,
      'user_id': user.pk,
      'username': user.username,
      'email': user.email,
    })

# Получение информации о пользователе
@api_view(['GET'])
def user_profile(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      user = request.user
      serializer = UserSerializer(user)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response({"message": "Необходимо авторизоваться"}, status=status.HTTP_401_UNAUTHORIZED)
