from rest_framework import serializers
from .models import MISAMusic

class MISAMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MISAMusic
        fields = ['full_name','dob','phone_number','email','job','work_unit','address','song_title','song_lyric','song_path', 'file_signature']
