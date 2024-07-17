### rest-frameworks
from rest_framework import serializers

### platforma.models
from .models import Kurs, Dars, Video, Comment, Like


###### MODELS SERIALIZERS #####

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'


class DarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dars
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class Emailserializers(serializers.Serializer):
    subject = serializers.CharField(max_length=155)
    massage = serializers.CharField()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

###### MODELS SERIALIZERS #####