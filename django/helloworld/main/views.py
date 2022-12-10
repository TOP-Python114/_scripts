from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        'main/base.html',
        {
            'head_title': 'Главная',
            'body_title': 'Добро пожаловать!',
            # 'align': 'center',
            'text': 'главная страница',
        }
    )

