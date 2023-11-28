from rest_framework import serializers
from .models import Employee,Singer,Song


class EmployeeSerializer(serializers.ModelSerializer):
    # employee_id = serializers.IntegerField(read_only = True)
    # first_name = serializers.CharField(max_length = 50)
    # last_name = serializers.CharField(max_length = 50)
    # department = serializers.CharField(max_length=40)
    # total_experience = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = "__all__"


class SingerSerializer(serializers.ModelSerializer):
    song = serializers.HyperlinkedRelatedField(view_name='song-detail',read_only = True,many=True)
    # song = serializers.StringRelatedField(read_only = True,many=True)
    class Meta:
        model = Singer
        fields = ['full_name','gender','song']

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ['title','duration','singer']        