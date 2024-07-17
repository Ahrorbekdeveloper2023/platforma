from django.conf import settings
from django.core.mail import send_mail

from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (KursSerializer,DarsSerializer,VideoSerializer,
                          CommentSerializer, Emailserializers,LikeSerializer)
from .permissions import UserPermission,AdminPermission
from .models import User, Kurs, Dars, Video, Comment, Like


class KursModelViewSet(ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    permission_classes = [AdminPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price']



class DarsModelViewSet(ModelViewSet):
    queryset = Dars.objects.all()
    serializer_class = DarsSerializer
    permission_classes = [AdminPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']

class VideoModelViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AdminPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['dars', 'video']


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [UserPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['video', 'text']


class EmailModelViewSet(APIView):
    def post(self,request:Request):

        serializer = Emailserializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        email_users=[]

        for user in users:
            email_users.append(user.email)
        email_users.append('ahrorbekmuhammadjonov653@gmail.com')


        send_mail(
            serializer.validated_data.get('subject'),
            serializer.validated_data.get('massage'),
            settings.EMAIL_HOST_USER,
            email_users,
            fail_silently=False,
        )
        return Response({"massage":"success"})

class LikeAPIView(APIView):

    def get(self, request, pk):
        likes = len(Like.objects.filter(like=True,video_id=pk))
        dislikes = len(Like.objects.filter(like=False,video_id=pk))
        return Response({'likes':likes,'dislikes': dislikes})


class LikeCreateViewSet(APIView):
    def post(self, request):
        try:
            likes_or_dislikes = Like.objects.filter(author_id=request.data.get("author"))
            for l_o_d in likes_or_dislikes:
                l_o_d.delete()
        except:
            pass

        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LikeSerializer(like_or_dislike).data)