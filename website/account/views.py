
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # Сохраняем пользователя
            user = serializer.save()
            # Возвращаем успешный ответ с данными нового пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные неверные, возвращаем ошибку
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def signin(request):
    if request.method == 'POST':
        # Получение данных из формы POST запроса
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            # Если пользователь аутентифицирован, выполняем вход
            login(request, user)
            return redirect('home')  # Перенаправляем пользователя на домашнюю страницу после успешного входа
        else:
            error_message = "Неверные учетные данные.\n Пожалуйста, попробуйте снова."
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')


def home(request):
    if request.method == 'POST':
        return redirect('signin')
    else:
        return render(request, 'home.html')

def news(request):
    if request.method == 'POST':
        return redirect('signin')
    else:
        return render(request, 'news.html')