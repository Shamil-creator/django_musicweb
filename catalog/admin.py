from django.contrib import admin
from .models import Author, Genre, Music, MusicInstance

admin.site.register(Music)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(MusicInstance)
