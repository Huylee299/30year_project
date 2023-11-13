from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse, HttpResponse
from .models import MISAMusic
from .serializers import MISAMusicSerializer
from ytmusicapi import YTMusic

# Create your views here.

@api_view(['POST'])
def register_song(request):
    if request.method == 'POST':
        ytmusic = YTMusic("browser.json")
        request_data = request.data
        if 'file' in request_data: 
            file = request_data['file']
            response = ytmusic.upload_song(file.temporary_file_path())
            if isinstance(response, str):
                misa_music = MISAMusic(
                    full_name = request_data['full_name'],
                    phone_number = request_data['phone_number'],
                    email = request_data['email'],
                    job = request_data['job'],
                    work_unit = request_data['work_unit'],
                    address = request_data['address'],
                    song_title = request_data['song_title'],
                    song_lyric = request_data['song_lyric'],
                    song_id = request_data['song_id'],
                    dob = request_data['dob'],
                )
                misa_music.save()
                return HttpResponse(response)
            else:
                return HttpResponse(response) if isinstance(response, str) else HttpResponse(response.reason)
        else: 
            return HttpResponse("EMPTY FILE")
        
    
@api_view(['GET'])
def get_songs(request):
    ytmusic = YTMusic("browser.json")
    musics = ytmusic.get_library_upload_songs()
    return HttpResponse(musics)

