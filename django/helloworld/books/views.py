from django.shortcuts import render

from random import choice

from .models import Book, Publisher


tips = (
    'Не печалься о том, что выходит за границы контроля. Не можешь изменить — нечего убиваться.',
    'То, что видишь перед собой, зависит от того, как именно на это смотришь.',
    'Обращай внимание только на советы, которые дают мудрые люди, заслужившие твое уважение.',
    'Верьте в тех, кто встретится на жизненном пути. Некоторые разочаруют, но будут и те, благодаря которым разочарование улетучится.',
    'Не ожидай, что кому-то захочется подарить тебе радость. Научись радовать себя самостоятельно, даже в одиночестве.',
    'То, от чего твое сердце счастливо трепещет, не обязательно сделает счастливым кого-то другого.',
    'В своих проблемах не ищи виноватых. Посмотри в зеркало.',
    'Уже не важно, что было раньше. Ещё не имеет значения, что будет дальше. Важен текущий момент, который нельзя упустить.'
)


def index_view(request):
    return render(
        request,
        'books/base.html',
        {
            'head_title': 'Главная',
            'body_title': 'Список книг',
            # 'align': 'center',
            'text': f"Совет дня:\n{choice(tips)}",
            'books': Book.objects.order_by('author', 'title'),
        }
    )


def publisher_view(request, pub_obj: Publisher):
    return render(
        request,
        'books/pubs.html',
        {
            'head_title': pub_obj.name,
            'body_title': f'Авторы и книги издательства {pub_obj.name}',
            'authors': pub_obj.authors.order_by('last_name')
        }
    )

