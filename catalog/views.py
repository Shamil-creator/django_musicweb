from django.shortcuts import render

# Create your views here.
from .models import Music, Author, MusicInstance, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_musics = Music.objects.all().count()
    num_instances = MusicInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = MusicInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_musics': num_musics, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


from django.views import generic


class MusicListView(generic.ListView):
    model = Music
