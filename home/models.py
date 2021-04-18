from django.db import models
# from django_mysql.models import ListTextField


class Song(models.Model):
    name=models.CharField(max_length=100)
    duration=models.IntegerField()
    upload_time=models.DateTimeField(auto_now_add=True)

class Podcast(models.Model):
    name=models.CharField(max_length=100)
    duration=models.IntegerField()
    upload_time=models.DateTimeField(auto_now_add=True)
    host=models.CharField(max_length=100)
    # participants =ListTextField(
    #     base_field=models.CharField(max_length=100),
    #     size=10,
    #     blank=True,
    # )
    
class AudioBook(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    narrator=models.CharField(max_length=100)
    duration=models.IntegerField()
    upload_time=models.DateTimeField(auto_now_add=True)
    
    
    
