from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите музыкальный жанр (например, рок, хип-хоп и т. д.)")

    def __str__(self):
        """Строка для представления объекта модели (в админке сайта и т.д.)"""
        return self.name


from django.urls import reverse  # Используется для создания URL-адреса путем изменения шаблонов url


class Music(models.Model):
    """Модель, представляющая собой пластинку (но не конкретную копию пластинки)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Author как строка, а не объект, потому что он еще не был объявлен в файле.
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание пластинки")
    genre = models.ManyToManyField(Genre, help_text="Укажите жанр пластинки")

    # ManyToManyField используется потому, что жанр может содержать много дисков. Диски могут охватывать многие жанры.
    # Класс Genre (Жанр) уже определен, поэтому мы можем указать объект выше.

    def __str__(self):
        """Строка для представления объекта модели."""
        return self.title

    def get_absolute_url(self):
        """Возвращает url-адрес для доступа к конкретному экземпляру пластинки."""
        return reverse('music-detail', args=[str(self.id)])


import uuid  # Требуется для уникальных экземпляров пластинок


class MusicInstance(models.Model):
    """Модель, представляющая конкретный экземпляр пластинки (то есть то, что можно взять в аренду)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Уникальный идентификатор для этой конкретной пластинки во всем магазине")
    music = models.ForeignKey('Music', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'техническое обслуживание'),
        ('o', 'у человека'),
        ('a', 'доступно'),
        ('r', 'зарезервированно'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='В наличии')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """для представления объекта модели"""
        return '%s (%s)' % (self.id, self.music.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Умер', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
