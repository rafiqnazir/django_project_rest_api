from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from home.models import Song,Podcast,AudioBook
from home.serializers import SongSerializer,AudioBookSerializer,PodcastSerializer
from rest_framework.views import APIView
from datetime import datetime



class GetView(APIView):
   
    def get_song_object(self, id):
        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    def get_podcast_object(self, id):
        try:
            return Podcast.objects.get(id=id)
        except Podcast.DoesNotExist:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    def get_audiobook_object(self, id):
        try:
            return AudioBook.objects.get(id=id)
        except AudioBook.DoesNotExist:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,type,id,format=None):
        if type.lower()=='song':
            song = self.get_song_object(id)
            serializer = SongSerializer(song)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif type.lower()=='podcast':
            podcast = self.get_podcast_object(id)
            serializer = PodcastSerializer(podcast)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif type.lower()=="audiobook":
            audiobook = self.get_audiobook_object(id)
            serializer = AudioBookSerializer(audiobook)
            return Response(serializer.data,status=status.HTTP_200_OK)
        data={}
        data["message"]="Audio Type Is Invalid"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


class ListAll(APIView):
    def get(self,request,type,format=None):
        if type.lower()=='song':
            song = Song.objects.all()
            serializer = SongSerializer(song,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif type.lower()=='podcast':
            podcast = Podcast.objects.all()
            serializer = PodcastSerializer(podcast,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif type.lower()=="audiobook":
            audiobook = AudioBook.objects.all()
            serializer = AudioBookSerializer(audiobook,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        data={}
        data["message"]="Audio Type Is Invalid"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
class PostView(APIView):
    
    def post_song(self,data):
        serializer = SongSerializer(Song(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post_podcast(self,data):
        serializer = PodcastSerializer(Podcast(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post_audiobook(self,data):
        serializer = AudioBookSerializer(AudioBook(), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request,type,format=None):
        if type.lower()=='song':
            return self.post_song(request.data)
        elif type.lower()=='podcast':
            return self.post_podcast(request.data)
        elif type.lower()=='audiobook':
            return self.post_audiobook(request.data)
        
        data={}
        data["message"]="Audio Type Is Invalid"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
class UpdateView(APIView):
    
    def update_song(self,id,data):
        try:
            song=Song.objects.get(id=id)
        except Song.DoesNotExist:
            raise Response( status=status.HTTP_400_BAD_REQUEST)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_podcast(self,id,data):
        try:
            podcast=Podcast.objects.get(id=id)
        except Podcast.DoesNotExist:
            raise Response( status=status.HTTP_400_BAD_REQUEST)
        serializer = PodcastSerializer(podcast, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_audiobook(self,id,data):
        try:
            audiobook=AudioBook.objects.get(id=id)
        except AudioBook.DoesNotExist:
            raise Response( status=status.HTTP_400_BAD_REQUEST)
        serializer = AudioBookSerializer(audiobook, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,type,id,format=None):
        if type.lower()=='song':
            return self.update_song(id,request.data)
        elif type.lower()=='podcast':
            return self.update_podcast(id,request.data)
        elif type.lower()=='audiobook':
            return self.update_audiobook(id,request.data)
        
        data={}
        data["message"]="Audio Type Is Invalid"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):
        
    def delete_song(self,id,format=None):
        try:
            song = Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        song.delete()
        data={}
        data["delete"]='Successfull'
        return Response(data,status=status.HTTP_200_OK)
    
    def delete_podcast(self,id,format=None):
        try:
            podcast = Podcast.objects.get(id=id)
        except Podcast.DoesNotExist:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        podcast.delete()
        data={}
        data["delete"]='Successfull'
        return Response(data,status=status.HTTP_200_OK)
    
    def delete_audiobook(self,id,format=None):
        try:
            audiobook = AudioBook.objects.get(id=id)
        except AudioBook.DoesNotExist:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
        audiobook.delete()
        data={}
        data["delete"]='Successfull'
        return Response(data,status=status.HTTP_200_OK)
        
    def delete(self, request,type, id, format=None):
        print("called")
        if type.lower()=='song':
            return self.delete_song(id)
        elif type.lower()=='podcast':
            return self.delete_podcast(id)
        elif type.lower()=='audiobook':
            return self.delete_audiobook(id)
        
        
        data={}
        data["message"]="Audio Type Is Invalid"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
        

    
    

