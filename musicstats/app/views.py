from django.shortcuts import redirect, render
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
            file_audio = request_data['file']
            file_audio_path = file_audio.temporary_file_path()
            response = ytmusic.upload_song(file_audio_path)
            if isinstance(response, str) and response == 'STATUS_SUCCEEDED':
                misa_music = MISAMusic(
                    full_name = request_data['full_name'],
                    phone_number = request_data['phone_number'],
                    email = request_data['email'],
                    job = request_data['job'],
                    work_unit = request_data['work_unit'],
                    address = request_data['address'],
                    song_title = request_data['song_title'],
                    song_lyric = request_data['song_lyric'],
                    song_path = file_audio_path,
                    file_signature = request_data['file_signature'],
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
    res = ytmusic.add_playlist_items("PLw-h3C8qbmkzW6nvnzqhItNRgOizR9NBO",
                                      ["V12Jp_LUCes"], duplicates=True)
    
    print(res)
    # musics = ytmusic.get_library_playlists()
    return HttpResponse(musics)


def add_playlist():
    ytmusic = YTMusic("browser.json")
    temp = ytmusic.add_playlist_items("PLw-h3C8qbmkzW6nvnzqhItNRgOizR9NBO",
                                      ["V12Jp_LUCes"])
    print(temp)
    return ""


