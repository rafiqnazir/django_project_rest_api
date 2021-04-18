from django.contrib import admin
from home.models import Song,AudioBook,Podcast

admin.site.register(Song)
admin.site.register(AudioBook)
admin.site.register(Podcast)