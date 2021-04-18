from rest_framework import serializers
from home.models import Song,AudioBook,Podcast

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','name','duration','upload_time']
        
class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id','name','duration','upload_time','host']
        
class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['id','author','title','narrator','duration','upload_time']