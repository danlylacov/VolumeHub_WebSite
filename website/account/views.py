from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.response import Response
from .serializers import  UserRegistrationSerializer
from .models import News



def home(request):
    if request.method == 'POST':
        return redirect('signin')
    else:
        return render(request, 'home.html')

def news(request):
    if request.method == 'POST':
        return redirect('signin')
    else:

        news = News.objects.all()
        print(news[0].id)

        return render(request, 'news.html', {'news': news})

def show_news(request, id):
    if request.method == 'POST':
        return redirect('signin')
    else:
        news = News.objects.get(id=id)
        return render(request, 'show_news.html', {"news": news})

@login_required
def settings(request):

    return render(request, 'settings.html')
























#----------------------------------------------------------------

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Неверные учетные данные.\n Пожалуйста, попробуйте снова."
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')








class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)